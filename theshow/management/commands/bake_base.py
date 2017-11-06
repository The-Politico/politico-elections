from core.aws import defaults, get_bucket
from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from geography.models import DivisionLevel


class BaseBakeCommand(object):
    """
    A mixin for baking election pages and context.

    fetch_ methods are used to collect elections to bake out.

    bake_ methods are overwritten in a child to render correct
    content string and key to bake.
    """
    bucket = get_bucket()

    STATE_LEVEL = DivisionLevel.objects.get(name=DIVISION_LEVELS['state'])

    def add_arguments(self, parser):
        parser.add_argument(
            '--election',
            required=True,
            help="Election date to bake out."
        )

    def bake(self, key, data, content_type):
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=data,
            CacheControl=defaults.CACHE_HEADER,
            ContentType=content_type
        )

    def fetch_federal_elex(self, election_day):
        """ TK. """
        return []

    def bake_federal_page(self, election_day, options):
        pass

    def fetch_state_elex(self, election_day):
        """ TK. """
        return []

    def bake_state_pages(self, election_day, options):
        pass

    def fetch_federal_executive_race_elex(self, election_day):
        """ TK. """
        return []

    def bake_federal_executive_race_page(self, election_day, options):
        pass

    def fetch_state_executive_race_elex(self, election_day):
        return [
            election for election in
            election_day.elections.all()
            if election.race.office.is_executive() and
            election.division.level == self.STATE_LEVEL
        ]

    def bake_state_executive_race_pages(self, election_day, options):
        pass

    def handle(self, *args, **options):
        print('> Baking!')

        election_day = ElectionDay.objects.get(date=options['election'])

        self.bake_federal_page(election_day, options)
        self.bake_state_pages(election_day, options)

        self.bake_federal_executive_race_page(election_day, options)
        self.bake_state_executive_race_pages(election_day, options)

        self.bake_federal_body_pages(election_day, options)
        self.bake_state_body_pages(election_day, options)

        print('Done.')
