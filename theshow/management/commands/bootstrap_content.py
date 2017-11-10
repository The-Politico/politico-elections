from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from tqdm import tqdm

from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from geography.models import Division, DivisionLevel
from theshow.models import PageContent


class Command(BaseCommand):
    help = 'Creates page content items for an election day.'

    def get_required_fixtures(self):
        self.NATIONAL_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['country'])
        self.STATE_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['state'])

    def add_arguments(self, parser):
        parser.add_argument(
            'elections',
            nargs='+',
            help="Election dates to create content for."
        )

    def create_legislative_office_page_content(self, election):
        """
        For legislative offices, create page content for the legislative
        Body the Office belongs to AND the Division that corresponds to
        that Body's Jurisdiction.

        E.g., for a Texas state senate seat, create page content for:
            - Texas state senate page
            - Texas state page
        """
        body = election.race.office.body
        division = election.race.office.body.jurisdiction.division
        PageContent.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(body),
            object_id=body.pk,
            election_day=election.election_day,
            division=division
        )
        PageContent.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(division),
            object_id=division.pk,
            election_day=election.election_day,
        )

    def create_federal_executive_state_pages_content(self, election):
        """
        Create state page content exclusively for the U.S. president.
        """
        content_type = ContentType.objects.get_for_model(election.race.office)
        for division in Division.objects.filter(level=self.STATE_LEVEL):
            PageContent.objects.get_or_create(
                content_type=content_type,
                object_id=election.race.office.pk,
                election_day=election.election_day,
                division=division
            )

    def create_executive_office_page_content(self, election):
        """
        For executive offices, create page content for the office.

        For the president, create pages for each
        """
        division = election.race.office.jurisdiction.division
        content_type = ContentType.objects.get_for_model(election.race.office)
        PageContent.objects.get_or_create(
            content_type=content_type,
            object_id=election.race.office.pk,
            election_day=election.election_day,
            division=division
        )
        if division.level == self.NATIONAL_LEVEL:
            self.create_federal_executive_state_pages_content(election)

    def route_election(self, election):
        """
        Legislative or executive office?
        """
        if election.race.office.body:
            self.create_legislative_office_page_content(election)
        else:
            self.create_executive_office_page_content(election)

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
