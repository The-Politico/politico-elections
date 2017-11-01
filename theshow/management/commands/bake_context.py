import os

from django.core.management.base import BaseCommand
from rest_framework.renderers import JSONRenderer
from tqdm import tqdm

from core.aws import defaults, get_bucket
from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from geography.models import DivisionLevel
from theshow.serializers import OfficeSerializer


class Command(BaseCommand):
    help = 'Bakes out context for an election.'
    bucket = get_bucket()

    def add_arguments(self, parser):
        parser.add_argument(
            'elections',
            nargs='+',
            help="Election dates to bake context for."
        )

    def bake(self, key, data):
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=data,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/json'
        )

    def bake_federal_page(self, election_day):
        pass

    def bake_state_pages(self, election_day):
        pass

    def bake_federal_executive_race_page(self, election_day):
        pass

    def bake_state_executive_race_pages(self, election_day):
        STATE_LEVEL = DivisionLevel.objects.get(name=DIVISION_LEVELS['state'])
        elections = [
            election for election in
            election_day.elections.all()
            if election.race.office.is_executive() and
            election.division.level == STATE_LEVEL
        ]
        print('> State executive races:')
        for election in tqdm(elections):
            serialized_data = JSONRenderer().render(
                OfficeSerializer(election.race.office, context={
                    'election_date': election_day.date
                }).data
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                election_day.cycle.slug,
                election.division.slug,
                election.race.office.slug.lower(),
                'context.json'
            )
            self.bake(key, serialized_data)

    def bake_federal_body_pages(self, election_day):
        pass

    def bake_state_body_pages(self, election_day):
        pass

    def handle(self, *args, **options):
        print('Baking context')

        elections = options['elections']

        for election in elections:
            election_day = ElectionDay.objects.get(date=election)

            self.bake_federal_page(election_day)
            self.bake_state_pages(election_day)

            self.bake_federal_executive_race_page(election_day)
            self.bake_state_executive_race_pages(election_day)

            self.bake_federal_body_pages(election_day)
            self.bake_state_body_pages(election_day)

        print('Done.')
