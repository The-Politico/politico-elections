import datetime

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Publishes an election!'

    def add_arguments(self, parser):
        parser.add_argument(
            'elections',
            nargs='+',
            help="Election dates to publish."
        )
        parser.add_argument(
            '--production',
            default=False,
            action='store_true',
            help="Publish to production"
        )

    def bake_production(self, election):
        print('Publishing {}'.format(election))
        call_command(
            'bake_context',
            '--election={}'.format(election),
            '--production'
        )
        call_command(
            'bake_statics',
            '--election={}'.format(election),
            '--hash={}'.format(self.hash),
            '--production'
        )
        call_command(
            'bake_pages',
            '--election={}'.format(election),
            '--hash={}'.format(self.hash),
            '--production'
        )

    def bake_staging(self, election):
        print('Publishing {}'.format(election))
        call_command(
            'bake_context',
            '--election={}'.format(election),
        )
        call_command(
            'bake_statics',
            '--election={}'.format(election),
            '--hash={}'.format(self.hash),
        )
        call_command(
            'bake_election',
            '--election={}'.format(election),
            '--hash={}'.format(self.hash),
        )

    def handle(self, *args, **options):
        elections = options['elections']
        self.hash = datetime.datetime.now().strftime("%s")
        for election in elections:
            if options['production']:
                self.bake_production(election)
            else:
                self.bake_staging(election)

        print('USA! USA! USA!')
