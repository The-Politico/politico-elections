import json
import os
import shutil
import subprocess
import urllib.request
import zipfile
from pathlib import Path

import shapefile
from django.core.management.base import BaseCommand
from results.models import Geography, GeographyLevel

FTP_BASE = 'ftp://ftp2.census.gov/geo/tiger/'
DATA_DIRECTORY = './data/geo/'


class Command(BaseCommand):
    help = 'Downloads and loads geo data for states and counties'

    def download_data(self, geo):
        TL_SLUG = 'tl_{}_us_{}'.format(self.YEAR, geo.lower())
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            TL_SLUG
        )
        ZIPFILE = '{}{}.zip'.format(DOWNLOAD_PATH, TL_SLUG)
        FTP_PATH = os.path.join(
            FTP_BASE,
            'TIGER{}'.format(self.YEAR),
            geo.upper(),
            'tl_{}_us_{}.zip'.format(self.YEAR, geo.lower())
        )

        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)

        if not Path(ZIPFILE).is_file():
            with urllib.request.urlopen(FTP_PATH) as response, \
                    open(ZIPFILE, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

        if not Path('{}{}.shp'.format(DOWNLOAD_PATH, TL_SLUG)).is_file():
            with zipfile.ZipFile(ZIPFILE, 'r') as file:
                file.extractall(DOWNLOAD_PATH)

    @staticmethod
    def toposimplify(geojson, p):
        """
        Convert geojson and simplify topology.
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

    def create_state_fixtures(self):
        TL_SLUG = 'tl_{}_us_state'.format(self.YEAR)
        DOWNLOAD_PATH = os.path.join(
            DATA_DIRECTORY,
            TL_SLUG
        )

        national, created = GeographyLevel.objects.get_or_create(
            label='national',
            code=0
        )
        NATION, created = Geography.objects.get_or_create(
            code='00',
            label='United States of America',
            state_fips='00',
            geography_level=national
        )

        shape = shapefile.Reader(os.path.join(
            DOWNLOAD_PATH,
            '{}.shp'.format(TL_SLUG)
        ))

        fields = shape.fields[1:]
        field_names = [f[0] for f in fields]
        level, created = GeographyLevel.objects.get_or_create(
            label='state',
            code=1
        )
        for shp in shape.shapeRecords():
            state = dict(zip(field_names, shp.record))
            print('>  {}'.format(state['STATEFP']))
            state_obj, created = Geography.objects.get_or_create(
                label=state['NAME'],
                code=state['STATEFP'],
                state_fips=state['STATEFP'],
                geography_level=level,
            )
            state_obj.geojson = self.toposimplify(
                shp.shape.__geo_interface__,
                '0.05'
            )
            state_obj.save()
            state_obj.parent.add(NATION)

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
        level, created = GeographyLevel.objects.get_or_create(
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
                geojson=shp.shape.__geo_interface__
            )

            county_obj.geojson = self.toposimplify(
                shp.shape.__geo_interface__,
                '0.075'
            )
            county_obj.save()
            county_obj.parent.add(state)

    def add_arguments(self, parser):
        parser.add_argument(
            'tigerline_year',
            type=str,
            help='Year of shapefile series'
        )

    def handle(self, *args, **options):
        self.YEAR = options['tigerline_year']

        print('Downloading data')
        self.download_data('state')
        self.download_data('county')

        print('Creating fixtures')
        self.create_state_fixtures()
        self.create_county_fixtures()
