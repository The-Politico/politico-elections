import json

from django.core.management.base import BaseCommand, CommandError
from results.models import Race
from uuslug import slugify

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def serialize_race_ids(self, races, field, second_field=None, file_prefix=None):
        values = races.values(field).distinct()

        for value in values:
            label = value[field]
            filters = {
                field: label
            }

            filtered_races = races.filter(**filters)
            
            if second_field:
                self.serialize_race_ids(filtered_races, second_field, file_prefix=label)
                continue

            race_ids = []
            for race in filtered_races:
                race_ids.append(race.ap_race_id)

            if file_prefix:
                filename = '{0}-{1}-ids.json'.format(
                    slugify(file_prefix), 
                    slugify(label)
                )
            else:
                filename = '{0}-ids.json'.format(slugify(label))


            with open('scripts/{0}'.format(filename), 'w') as f:
                json.dump(race_ids, f)



    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        races = Race.objects.filter(
            election__date=options['election_date'],
        )
        
        self.serialize_race_ids(races, 'seat__geography__label')
        self.serialize_race_ids(races, 'seat__office__label')
        self.serialize_race_ids(
            races, 
            'seat__geography__label',
            second_field='seat__office__label'
        )