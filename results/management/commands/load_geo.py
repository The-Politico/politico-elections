import json
import os
import shutil
import subprocess
import urllib.request as request
import zipfile
from pathlib import Path

import geojson
import shapefile
from django.core.management.base import BaseCommand, CommandError
from results.models import Geography, GeoJson, GeoLevel

SHP_BASE = 'https://www2.census.gov/geo/tiger/GENZ{}/shp/'
DATA_DIRECTORY = './data/geo/'

NATION_LEVEL, created = GeoLevel.objects.get_or_create(
    label='national',
    code=0
)
STATE_LEVEL, created = GeoLevel.objects.get_or_create(
    label='state',
    code=1
)
COUNTY_LEVEL, created = GeoLevel.objects.get_or_create(
    label='county',
    code=3
)

NATION, created = Geography.objects.get_or_create(
    geocode='00',
    label='United States of America',
    geolevel=NATION_LEVEL
)


class Command(BaseCommand):
    help = 'Downloads and loads geo data for states and counties from \
    U.S. Census Bureau simplified cartographic boundary files.'

    def download_shp_data(self, geo):
        SHP_SLUG = 'cb_{}_us_{}_500k'.format(self.YEAR, geo.lower())
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            SHP_SLUG
        )
        ZIPFILE = '{}{}.zip'.format(DOWNLOAD_PATH, SHP_SLUG)
        SHP_PATH = os.path.join(
            SHP_BASE.format(self.YEAR),
            SHP_SLUG
        )

        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)

        if not Path(ZIPFILE).is_file():
            with request.urlopen('{}.zip'.format(SHP_PATH)) as response,\
                    open(ZIPFILE, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

        if not Path('{}{}.shp'.format(DOWNLOAD_PATH, SHP_SLUG)).is_file():
            with zipfile.ZipFile(ZIPFILE, 'r') as file:
                file.extractall(DOWNLOAD_PATH)

    @staticmethod
    def toposimplify(geojson, p):
        """
        Convert geojson and simplify topology.

        geojson is a dict representing geojson.
        p is a simplification threshold value between 0 and 1.
        """
        proc_out = subprocess.run(
            ['geo2topo'],
            input=bytes(
                json.dumps(geojson),
                'utf-8'),
            stdout=subprocess.PIPE
        )
        proc_out = subprocess.run(
            ['toposimplify', '-P', p],
            input=proc_out.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )
        return json.loads(proc_out.stdout)

    def get_county_shp(self, fips):
        SHP_SLUG = 'cb_{}_us_county_500k'.format(self.YEAR)
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            SHP_SLUG
        )
        shape = shapefile.Reader(os.path.join(
            DOWNLOAD_PATH,
            '{}.shp'.format(SHP_SLUG)
        ))
        fields = shape.fields[1:]
        field_names = [f[0] for f in fields]
        county_records = [
            shp for shp in shape.shapeRecords()
            if dict(zip(field_names, shp.record))['STATEFP'] == fips or
            fips == '00'
        ]
        features = []
        for shp in county_records:
            record = dict(zip(field_names, shp.record))
            geometry = shp.shape.__geo_interface__
            geodata = {
                'type': 'Feature',
                'geometry': geometry,
                'properties': {
                    'state': record['STATEFP'],
                    'county': record['COUNTYFP'],
                    'name': record['NAME']
                }
            }
            features.append(geodata)
        threshold = self.THRESHOLDS['nation'] if fips == '00' else \
            self.THRESHOLDS['county']
        return self.toposimplify(
            geojson.FeatureCollection(features),
            threshold
        )

    def create_nation_fixtures(self):
        SHP_SLUG = 'cb_{}_us_state_500k'.format(self.YEAR)
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            SHP_SLUG
        )

        shape = shapefile.Reader(os.path.join(
            DOWNLOAD_PATH,
            '{}.shp'.format(SHP_SLUG)
        ))
        fields = shape.fields[1:]
        field_names = [f[0] for f in fields]
        features = []
        for shp in shape.shapeRecords():
            state = dict(zip(field_names, shp.record))
            geodata = {
                'type': 'Feature',
                'geometry': shp.shape.__geo_interface__,
                'properties': {
                    'state': state['STATEFP'],
                    'name': state['NAME']
                }
            }
            features.append(geodata)
        GeoJson.objects.update_or_create(
            geography=NATION,
            geography_level=STATE_LEVEL,
            simplification=self.THRESHOLDS['nation'],
            defaults={
                'topojson': self.toposimplify(
                    geojson.FeatureCollection(features),
                    self.THRESHOLDS['nation']
                ),
            },
        )

        geo, created = GeoJson.objects.update_or_create(
            geography=NATION,
            geography_level=COUNTY_LEVEL,
            simplification=self.THRESHOLDS['nation'],
            defaults={
                'topojson': self.get_county_shp('00'),
            },
        )
        print('>  FIPS {}  @ ~{}kb'.format(
            '00',
            round(len(json.dumps(geo.topojson)) / 1000)
        ))

    def create_state_fixtures(self):
        SHP_SLUG = 'cb_{}_us_state_500k'.format(self.YEAR)
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            SHP_SLUG
        )

        shape = shapefile.Reader(os.path.join(
            DOWNLOAD_PATH,
            '{}.shp'.format(SHP_SLUG)
        ))
        fields = shape.fields[1:]
        field_names = [f[0] for f in fields]

        for shp in shape.shapeRecords():
            state = dict(zip(field_names, shp.record))
            state_obj, created = Geography.objects.get_or_create(
                label=state['NAME'],
                geocode=state['STATEFP'],
                geolevel=STATE_LEVEL,
                parent=NATION
            )
            geodata = {
                'type': 'Feature',
                'geometry': shp.shape.__geo_interface__,
                'properties': {
                    'state': state['STATEFP'],
                    'name': state['NAME']
                }
            }
            geojson, created = GeoJson.objects.update_or_create(
                geography=state_obj,
                geography_level=STATE_LEVEL,
                simplification=self.THRESHOLDS['state'],
                defaults={
                    'topojson': self.toposimplify(
                        geodata,
                        self.THRESHOLDS['state']
                    ),
                },
            )
            geojson, created = GeoJson.objects.update_or_create(
                geography=state_obj,
                geography_level=COUNTY_LEVEL,
                simplification=self.THRESHOLDS['county'],
                defaults={
                    'topojson': self.get_county_shp(state['STATEFP']),
                },
            )
            print('>  FIPS {}  @ ~{}kb'.format(
                state['STATEFP'],
                round(len(json.dumps(geojson.topojson)) / 1000)
            ))

    def create_county_fixtures(self):
        TL_SLUG = 'tl_{}_us_county'.format(self.YEAR)
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            TL_SLUG
        )
        shape = shapefile.Reader(os.path.join(
            DOWNLOAD_PATH,
            '{}.shp'.format(TL_SLUG)
        ))

        fields = shape.fields[1:]
        field_names = [f[0] for f in fields]
        level, created = GeoLevel.objects.get_or_create(
            label='county',
            code=3
        )
        for shp in shape.shapeRecords():
            county = dict(zip(field_names, shp.record))
            print('>  {}'.format(county['GEOID']))
            state = Geography.objects.get(code=county['STATEFP'])
            county_obj, created = Geography.objects.get_or_create(
                label=county['NAME'],
                code=county['GEOID'],
                geography_level=level,
                state_fips=county['STATEFP'],
            )
            county_obj.geojson = self.toposimplify(
                shp.shape.__geo_interface__,
                self.THRESHOLDS['county']
            )
            county_obj.save()
            county_obj.parent.add(state)
            print('>  FIPS {}  @ ~{}kb'.format(
                county['GEOID'],
                round(len(json.dumps(county_obj.geojson)) / 1000)
            ))

    def add_arguments(self, parser):
        def check_threshold(arg):
            value = float(arg)
            if value < 0 or value > 1:
                raise CommandError(
                    'Threshold must be a decimal between 0 and 1.'
                )
            return value

        parser.add_argument(
            '--year',
            action='store',
            dest='year',
            default='2016',
            help='Specify year of shapefile series (default, 2016)',
        )
        parser.add_argument(
            '--states',
            action='store_true',
            dest='states',
            help='Just load states',
        )
        parser.add_argument(
            '--counties',
            action='store_true',
            dest='counties',
            help='Just load counties',
        )
        parser.add_argument(
            '--nationThreshold',
            type=check_threshold,
            default=0.005,
            dest='nationThreshold',
            help='Simplification threshold value for nation topojson \
                (default, 0.005)'
        )
        parser.add_argument(
            '--stateThreshold',
            type=check_threshold,
            default=0.05,
            dest='stateThreshold',
            help='Simplification threshold value for state topojson \
                (default, 0.05)'
        )
        parser.add_argument(
            '--countyThreshold',
            type=check_threshold,
            default=0.075,
            dest='countyThreshold',
            help='Simplification threshold value for county topojson \
                (default, 0.075)'
        )

    def handle(self, *args, **options):
        self.YEAR = options['year']
        self.THRESHOLDS = {
            'nation': str(options['nationThreshold']),
            'state': str(options['stateThreshold']),
            'county': str(options['countyThreshold']),
        }

        if options['counties'] and options['states']:
            raise CommandError('Can\'t load only counties and only states...')

        print('Downloading data')
        self.download_shp_data('state')
        self.download_shp_data('county')

        print('Creating fixtures')
        self.create_nation_fixtures()
        if not options['counties']:
            self.create_state_fixtures()
        # if not options['states']:
        #     self.create_county_fixtures()
        self.stdout.write(
            self.style.SUCCESS('Finished loading geography fixtures.')
        )
