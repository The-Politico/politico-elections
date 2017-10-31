import json
import os
import statistics

import boto3
from census import Census
from django.core.management.base import BaseCommand
from tqdm import tqdm

from core.constants import DIVISION_LEVELS
from demographic.models import CensusEstimate, CensusTable
from geography.models import Division, DivisionLevel

census = Census(os.getenv('CENSUS_API_KEY'))

STATE_LEVEL = DivisionLevel.objects.get(name=DIVISION_LEVELS['state'])
COUNTY_LEVEL = DivisionLevel.objects.get(name=DIVISION_LEVELS['county'])

OUTPUT_PATH = 'election-results/data/us-census'

CACHE_HEADER = str('max-age=300')


def get_bucket():
    session = boto3.session.Session(
        region_name='us-east-1',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(os.getenv('AWS_S3_PUBLISH_BUCKET'))
    return bucket


class Command(BaseCommand):
    help = 'Gathers census data from the Census API and outputs JSON to S3.'

    @staticmethod
    def get_series(series):
        """
        Returns a census series API handler.
        """
        if series == 'acs1':
            return census.acs1dp
        elif series == 'acs5':
            return census.acs5
        elif series == 'sf1':
            return census.sf1
        elif series == 'sf3':
            return census.sf3
        else:
            return None

    @staticmethod
    def write_estimate(table, variable, code, datum):
        """
        Creates new estimate from a census series.

        Data has following signature from API:
        {
            'B00001_001E': '5373',
             'NAME': 'Anderson County, Texas',
             'county': '001',
             'state': '48'
        }
        """
        try:
            division = Division.objects.get(code='{}{}'.format(
                datum['state'],
                datum['county']
            ), level=COUNTY_LEVEL)
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={
                    'estimate': datum[code] or 0
                }
            )
        except:
            print ('ERROR: {}, {}'.format(datum['NAME'], datum['state']))

    def get_county_estimates_by_state(
        self, api, table, variable, estimate, state
    ):
        """
        Calls API for all counties in a state and a given estimate.
        """
        state = Division.objects.get(level=STATE_LEVEL, code=state)
        county_data = api.get(
            ('NAME', estimate),
            {
                'for': 'county:*',
                'in': 'state:{}'.format(state.code)
            },
            year=table.year
        )
        for datum in county_data:
            self.write_estimate(table, variable, estimate, datum)

    def fetch_census_data(self, states):
        """
        Fetch census estimates from table.
        """
        print('Fetching census data')
        for table in CensusTable.objects.all():
            api = self.get_series(table.series)
            for variable in table.variables.all():
                estimate = '{}_{}'.format(
                    table.code,
                    variable.code
                )
                print('>> Fetching {} {} {}'.format(
                    table.year,
                    table.series,
                    estimate
                ))
                for state in tqdm(states):
                    self.get_county_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )

    @staticmethod
    def aggregate_variable(estimate, code):
        """
        Aggregate census table variables by a custom label.
        """
        estimates = [
            variable.estimates.get(division__code=code).estimate
            for variable in estimate.variable.label.variables.all()
        ]
        method = estimate.variable.label.aggregation
        if method == 's':
            aggregate = sum(estimates)
        elif method == 'a':
            aggregate = statistics.mean(estimates)
        elif method == 'm':
            aggregate = statistics.median(estimates)
        else:
            aggregate = None
        return aggregate

    def aggregate_counties(self, parent):
        """
        Aggregates county-level estimates within a given state.

        Creates data structure designed for an export in this format:
        .../{series}/{year}/{state}/{table}.json
        """
        data = {}
        for division in tqdm(
            Division.objects.filter(level=COUNTY_LEVEL, parent=parent)
        ):
            fips = division.code
            aggregated_labels = []  # Keep track of already agg'ed variables
            for estimate in division.census_estimates.all():
                series = estimate.variable.table.series
                year = estimate.variable.table.year
                table = estimate.variable.table.code
                label = estimate.variable.label.label
                code = estimate.variable.code
                if series not in data:
                    data[series] = {}
                if year not in data[series]:
                    data[series][year] = {}
                if table not in data[series][year]:
                    data[series][year][table] = {}
                if fips not in data[series][year][table]:
                    data[series][year][table][fips] = {}
                if label is not None:
                    if label not in aggregated_labels:
                        aggregated_labels.append(label)
                        data[series][year][table][fips][label] \
                            = self.aggregate_variable(estimate, fips)
                else:
                    data[series][year][table][division.code][code] \
                        = estimate.estimate
        return data

    @staticmethod
    def export_state_files(bucket, state, data):
        for series in data.keys():
            for year in data[series].keys():
                for table in data[series][year].keys():
                    key = os.path.join(
                        OUTPUT_PATH,
                        series,
                        year,
                        state.code,
                        '{}.json'.format(table)
                    )
                    bucket.put_object(
                        Key=key,
                        ACL='public-read',
                        Body=json.dumps(data[series][year][table]),
                        CacheControl=CACHE_HEADER,
                        ContentType='application/json'
                    )

    def export_by_state(self, states):
        bucket = get_bucket()
        for fips in states:
            state = Division.objects.get(level=STATE_LEVEL, code=fips)
            print('>> Exporting: {}'.format(state.code))
            state_data = self.aggregate_counties(state)
            self.export_state_files(bucket, state, state_data)

    def add_arguments(self, parser):
        parser.add_argument(
            'states',
            nargs='+',
            help="States to export by FIPS code. Use '+' for all."
        )
        parser.add_argument(
            '--export',
            action='store_true',
            dest='export',
            default=False,
            help="Export existing estimates for states only. "
            "Don't fetch estimates from Census API."
        )

    def handle(self, *args, **options):
        states = options['states']
        if options['export'] is False:
            self.fetch_census_data(states)
        self.export_by_state(states)
        print("Done.")
