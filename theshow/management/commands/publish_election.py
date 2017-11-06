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

    def handle(self, *args, **options):
        elections = options['elections']
        hash = datetime.datetime.now().strftime("%s")
        for election in elections:
            print('Publishing {}'.format(election))

            call_command(
                'bake_context',
                '--election={}'.format(election)
            )
            call_command(
                'bake_statics',
                '--election={}'.format(election),
                '--hash={}'.format(hash)
            )
            call_command(
                'bake_election',
                '--election={}'.format(election),
                '--hash={}'.format(hash)
            )

        print('USA! USA! USA!')
