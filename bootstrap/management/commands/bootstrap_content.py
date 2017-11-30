from django.core.management.base import BaseCommand
from tqdm import tqdm

from bootstrap.methods.content import BootstrapContentMethods
from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from entity.models import Jurisdiction
from geography.models import DivisionLevel


class Command(BaseCommand, BootstrapContentMethods):
    help = 'Creates page content items  for an election day. More TK.'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.NATIONAL_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['country'])
        self.STATE_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['state'])
        self.FEDERAL_JURISDICTION = Jurisdiction.objects.get(
            division__level=self.NATIONAL_LEVEL)

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
            self.bootstrap_special_election(election)
        elif election.race.office.body:
            self.bootstrap_legislative_office(election)
        else:
            self.bootstrap_executive_office(election)

    def handle(self, *args, **options):
        print('Bootstrapping page content')
        election_dates = options['elections']

        for election_date in election_dates:
            print('> {}'.format(election_date))
            election_day = ElectionDay.objects.get(date=election_date)
            for election in tqdm(election_day.elections.all()):
                self.route_election(election)
        print('Done.')
