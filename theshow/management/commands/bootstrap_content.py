from django.core.management.base import BaseCommand
from tqdm import tqdm

from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from entity.models import Jurisdiction
from geography.models import DivisionLevel
from theshow.utils.bootstrap.content import (create_executive_office_page_content,
                                             create_federal_executive_state_pages_content,
                                             create_legislative_office_page_content,
                                             create_special_election_page_content)


class Command(BaseCommand):
    help = 'Creates page content items  for an election day. More TK.'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.create_executive_office_page_content = \
            create_executive_office_page_content
        self.create_legislative_office_page_content = \
            create_legislative_office_page_content
        self.create_federal_executive_state_pages_content = \
            create_federal_executive_state_pages_content
        self.create_special_election_page_content = \
            create_special_election_page_content

    def get_required_fixtures(self):
        self.NATIONAL_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['country'])
        self.STATE_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['state'])
        self.FEDERAL_JURISDICTION = Jurisdiction.objects.get(
            division__level=self.NATIONAL_LEVEL
        )

    def add_arguments(self, parser):
        parser.add_argument(
            'elections',
            nargs='+',
            help="Election dates to create content for."
        )

    def route_election(self, election):
        """
        Legislative or executive office?
        """
        if election.race.special:
            self.create_special_election_page_content(self, election)
        elif election.race.office.body:
            self.create_legislative_office_page_content(self, election)
        else:
            self.create_executive_office_page_content(self, election)

    def handle(self, *args, **options):
        print('Bootstrapping page content')
        self.get_required_fixtures()
        election_dates = options['elections']

        for election_date in election_dates:
            print('> {}'.format(election_date))
            election_day = ElectionDay.objects.get(date=election_date)
            for election in tqdm(election_day.elections.all()):
                self.route_election(election)
        print('Done.')
