import json

from django.core.management.base import BaseCommand, CommandError
from election.models import Election
from uuslug import slugify

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def serialize_race_ids(self, elections, field, second_field=None, file_prefix=None):
        # get distinct values for field from passed elections queryset
        values = elections.values(field).distinct()

        # loop through our distinct values to build a list of elections
        # for each value
        for value in values:
            # get the label out of the object
            label = value[field]

            # build dict for passing as kwarg
            filters = {
                field: label
            }

            # filter elections based on current value
            filtered_races = elections.filter(**filters)
            
            # BEFORE WE BUILD OUR FILE, check if we need to do this again
            # at a second level
            if second_field:
                self.serialize_race_ids(filtered_races, second_field, file_prefix=label)
                continue

            # loop through our filtered elections to get the race id
            race_ids = []   
            for race in filtered_races:
                race_ids.append(race.apelectionmeta_set.all()[0].ap_election_id)

            # build our file of race ids
            if file_prefix:
                filename = '{0}-{1}-elections.json'.format(
                    slugify(file_prefix), 
                    slugify(label)
                )
            else:
                filename = '{0}-elections.json'.format(slugify(label))

            with open('output/elections/{0}'.format(filename), 'w') as f:
                json.dump(race_ids, f)



    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        elections = Election.objects.filter(
            election_day__date=options['election_date'],
        )
        
        self.serialize_race_ids(elections, 'race__office__division__code')
        self.serialize_race_ids(elections, 'race__office__body__name')
        self.serialize_race_ids(
            elections, 
            'race__office__division__code',
            second_field='race__office__body__name'
        )