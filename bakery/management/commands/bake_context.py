from django.core.management.base import BaseCommand

from bakery.methods.context import BakeContextMethods
from core.aws import defaults, get_bucket
from core.constants import DIVISION_LEVELS
from election.models import ElectionDay
from geography.models import DivisionLevel


class Command(BakeContextMethods, BaseCommand):
    help = 'Bakes out context for an election.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--election',
            required=True,
            help="Election date to bake out."
        )

        parser.add_argument(
            '--production',
            action='store_true',
            default=False,
            help="Publish to production"
        )

    def bake(self, key, data, content_type, production=False):
        bucket = get_bucket(production)
        bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=data,
            CacheControl=defaults.CACHE_HEADER,
            ContentType=content_type
        )

    def handle(self, *args, **options):
        print('> Baking Context JSON!')
        self.NATIONAL_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['country'])
        self.STATE_LEVEL = DivisionLevel.objects.get(
            name=DIVISION_LEVELS['state'])
        self.ELECTION_DAY = ElectionDay.objects.get(
            date=options['election']
        )
        super(Command, self).handle(*args, **options)
