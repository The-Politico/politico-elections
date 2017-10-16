import json

from django.core.management.base import BaseCommand, CommandError
from results.models import Race
from uuslug import slugify

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def serialize_race_ids(self, races, field, second_field=None, file_prefix=None):
        # get distinct values for field from passed races queryset
        values = races.values(field).distinct()

        # loop through our distinct values to build a list of races
        # for each value
        for value in values:
            # get the label out of the object
            label = value[field]

            # build dict for passing as kwarg
            filters = {
                field: label
            }

            # filter races based on current value
            filtered_races = races.filter(**filters)
            
            # BEFORE WE BUILD OUR FILE, check if we need to do this again
            # at a second level
            if second_field:
                self.serialize_race_ids(filtered_races, second_field, file_prefix=label)
                continue

            # loop through our filtered races to get the race id
            race_ids = []   
            for race in filtered_races:
                race_ids.append(race.ap_race_id)

            # build our file of race ids
            if file_prefix:
                filename = '{0}-{1}-races.json'.format(
                    slugify(file_prefix), 
                    slugify(label)
                )
            else:
                filename = '{0}-races.json'.format(slugify(label))

            with open('output/races/{0}'.format(filename), 'w') as f:
                json.dump(race_ids, f)



    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        races = Race.objects.filter(
            election__date=options['election_date'],
        )
        
        self.serialize_race_ids(races, 'office__geography__label')
        self.serialize_race_ids(races, 'office__body__label')
        self.serialize_race_ids(
            races, 
            'office__geography__label',
            second_field='office__body__label'
        )