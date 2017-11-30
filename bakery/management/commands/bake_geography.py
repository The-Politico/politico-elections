import json
import os

from django.core.management.base import BaseCommand
from tqdm import tqdm

from core.aws import defaults, get_bucket
from core.constants import DIVISION_LEVELS
from geography.models import Division, DivisionLevel

OUTPUT_PATH = os.path.join(
    defaults.ROOT_PATH,
    'data/geography/2016'  # TODO FACTOR OUT YEAR..
)


class Command(BaseCommand):
    help = 'Uploads county-level topojson by state.'

    def add_arguments(self, parser):
        parser.add_argument(
            'states',
            nargs='+',
            help="States to export by FIPS code."
        )

    def handle(self, *args, **options):
        print('Exporting geographies')

        states = options['states']
        bucket = get_bucket(production=True)

        STATE_LEVEL = DivisionLevel.objects.get(name=DIVISION_LEVELS['state'])
        COUNTY_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['county'])

        for state in tqdm(states):
            division = Division.objects.get(level=STATE_LEVEL, code=state)
            # TODO Add a concept of years
            geography = division.geographies.get(
                subdivision_level=COUNTY_LEVEL
            )
            key = os.path.join(
                OUTPUT_PATH,
                'state',
                division.code,
                'counties.json'
            )
            bucket.put_object(
                Key=key,
                ACL=defaults.ACL,
                Body=json.dumps(geography.topojson),
                CacheControl=defaults.CACHE_HEADER,
                ContentType='application/json'
            )
