import json

from django.core.management.base import BaseCommand, CommandError
from results.models import Race
from uuslug import slugify

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        races = Race.objects.filter(
            election__date=options['election_date'],
        )
        states = races.values('seat__geography__label').distinct()
        offices = races.values('seat__office__label').distinct()

        for state_obj in states:
            state = state_obj['seat__geography__label']
            state_races = races.filter(
                seat__geography__label=state
            )
            race_ids = []

            for race in state_races:
                race_ids.append(race.ap_race_id)

            with open(
                'scripts/{0}-races.json'.format(slugify(state)), 
                'w'
            ) as f:
                json.dump(race_ids, f)

        for office_obj in offices:
            office = office_obj['seat__office__label']
            office_races = races.filter(
                seat__office__label=office
            )
            race_ids = []

            for race in office_races:
                race_ids.append(race.ap_race_id)

            with open(
                'scripts/{0}-races.json'.format(slugify(office)),
                'w'
            ) as f:
                json.dump(race_ids, f)
