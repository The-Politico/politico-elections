import os
import statistics

from census import Census
from django.core.management.base import BaseCommand
from tqdm import tqdm

from demographic.models import CensusEstimate, CensusTable
from geography.models import Division, DivisionLevel

census = Census(os.getenv('CENSUS_API_KEY'))

STATE_LEVEL = DivisionLevel.objects.get(name='state')


class Command(BaseCommand):
    help = 'Gathers census data from the Census API and outputs a master json \
    by county'

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
            ))
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={
                    'estimate': datum[code] or 0
                }
            )
        except:
            print ('ERROR: {}, {}'.format(datum['NAME'], datum['state']))

    def get_estimates_by_county_state(self, api, table, variable, estimate):
        for state in tqdm(Division.objects.filter(level=STATE_LEVEL)):
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

    def fetch_census_data(self):
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
                print('>> {} - {}'.format(estimate, table.year))
                self.get_estimates_by_county_state(
                    api=api,
                    table=table,
                    variable=variable,
                    estimate=estimate
                )

    @staticmethod
    def aggregate_variable(estimate, fips):
        """
        Aggregate census table variables by a custom label.
        """
        estimates = [
            variable.estimates.get(division__code=fips).estimate
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

    def export_data(self):
        print("Exporting data")
        data = {}
        for division in tqdm(Division.objects.all()):
            data[division.code] = {}
            aggregated_labels = []  # Keep track of already agg'ed variables
            for estimate in division.census_estimates.all():
                table = estimate.variable.table.code
                if table not in data[division.code]:
                    data[division.code][table] = {}
                label = estimate.variable.label
                if label is not None:
                    if label not in aggregated_labels:
                        aggregated_labels.append(estimate.variable.label)
                        data[division.code][table][label.label] = \
                            self.aggregate_variable(estimate, division.code)
                else:
                    data[division.code][table][estimate.variable.code] = \
                        estimate.estimate
            # TODO: write exports...
            # export(data[fips.code], fips.code, "census/fips")
            # export(data, 'all', 'census')

    def handle(self, *args, **options):
        print("Beginning census run")
        self.fetch_census_data()
        self.export_data()
        print("Done.")
