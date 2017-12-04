# This is ugly. I'm sorry.

import csv
import json
import os
import re
from functools import reduce
from io import StringIO
from itertools import groupby

import agate
import requests
import us
from census import Census
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.aws import defaults, get_bucket

url = (
    "https://raw.githubusercontent.com/openelections/openelections-data-us/"
    "master/2016/20161108__us__general__president__county.csv"
)

# TODO: de-uglify all this....
OUTPUT_PATH = os.path.join(
    defaults.ROOT_PATH,
    'cdn/historical-results/2016-11-08/president'
)


GOP_PARTY_NAMES = ['R', 'Republican Party']
DEM_PARTY_NAMES = ['D', 'Democratic Party']


def county_clean(name):
    name = name.lower()
    name = name.replace(' county', '')
    return name


def county_standardizer(name):
    name = name.lower()
    name = re.sub(r'^st ', 'st. ', name)
    return name


def lookup_fips(name, counties, state):
    county = filter(
        lambda c: county_clean(c['NAME']) == county_standardizer(name),
        counties
    )
    try:
        return '{}{}'.format(state, list(county)[0]['county'])
    except:
        print('ERROR: {}'.format(name))
        return 'XXXXX'


class Command(BaseCommand):
    help = (
        'Bootstraps previous election results.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            'states',
            nargs='+',
            help="States to export by FIPS code."
        )

    @staticmethod
    def summarize_total_votes(state_results):
        sorted_results = sorted(state_results, key=lambda k: k['fips'])
        grouped_results = groupby(sorted_results, key=lambda c: c['fips'])
        total_votes = [
            reduce(lambda x, y: {
                "fips": x['fips'],
                "votes": int(x['votes']) + int(y['votes'])
            }, values)
            for k, values in grouped_results
        ]
        return {
            f['fips']: f['votes']
            for f in total_votes
        }

    def handle(self, *args, **options):
        bucket = get_bucket(True)
        census = Census(os.getenv('CENSUS_API_KEY'))

        response = requests.get(url)
        f = StringIO(response.content.decode('utf-8'))
        reader = csv.DictReader(f, delimiter=',')
        records = [r for r in reader]
        states = options['states']

        for state in states:
            postal = us.states.lookup(state).abbr
            counties = census.sf1.get('NAME', geo={
                'for': 'county:*',
                'in': 'state:{}'.format(state)
            })
            state_results = [
                {
                    **r,
                    **{"fips": lookup_fips(r['county'], counties, state)}
                }
                for r in records if r['state'] == postal and
                r['county'] != 'Total'
            ]

            total_votes = self.summarize_total_votes(state_results)

            gop_results = [
                {
                    "party": 'GOP', "fips": r['fips'],
                    "votes": int(r['votes']),
                    "total_votes": total_votes[r['fips']],
                }
                for r in
                list(filter(
                    lambda row: row['party'] in GOP_PARTY_NAMES,
                    state_records
                ))]
            dem_results = [
                {
                    "party": 'Dem', "fips": r['fips'],
                    "votes": int(r['votes']),
                    "total_votes": total_votes[r['fips']],
                }
                for r in
                list(filter(
                    lambda row: row['party'] in DEM_PARTY_NAMES,
                    state_records
                ))]

            all_results = dem_results + gop_results

            key = os.path.join(
                OUTPUT_PATH,
                slugify(us.states.lookup(state).name),
                'data.json'
            )
            bucket.put_object(
                Key=key,
                ACL=defaults.ACL,
                Body=json.dumps(all_results),
                CacheControl=defaults.CACHE_HEADER,
                ContentType='application/json'
            )
