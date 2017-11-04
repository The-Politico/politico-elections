import os

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from tqdm import tqdm

from core.aws import defaults, get_bucket
from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from geography.models import DivisionLevel
from theshow.views import StateExecutiveRacePageExport


class Command(BaseCommand):
    help = 'Bakes pages for an election.'
    bucket = get_bucket()

    def add_arguments(self, parser):
        parser.add_argument(
            'elections',
            nargs='+',
            help="Election dates to bake pages for."
        )

    def bake(self, key, data):
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=data,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='text/html'
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
            context = StateExecutiveRacePageExport.build_context(
                election_datestring=election.election_day.__str__(),
                state_slug=election.division.slug,
                office_slug=election.race.office.slug,
            )
            template_string = render_to_string(
                StateExecutiveRacePageExport.template_name,
                context
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                election_day.cycle.slug,
                election.division.slug,
                election.race.office.slug.lower(),
                'index.html'
            )
            self.bake(key, template_string)

    def bake_federal_body_pages(self, election_day):
        pass

    def bake_state_body_pages(self, election_day):
        pass

    def handle(self, *args, **options):
        print('Baking election pages')

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
