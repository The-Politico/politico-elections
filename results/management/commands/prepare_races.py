import json

from django.core.management.base import BaseCommand, CommandError
from results.models import Race

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)
        parser.add_argument('state_name', type=str)

    def handle(self, *args, **options):
        races = Race.objects.filter(
            election__date=options['election_date'],
            seat__geography__label=options['state_name'].capitalize()
        )

        ids = []
        for race in races:
            ids.append(race.ap_race_id)

        with open('scripts/{0}-races.json'.format(
            options['state_name']
        ), 'w') as f:
            json.dump(ids, f)