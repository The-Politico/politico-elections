import os

from django.core.management.base import BaseCommand
from rest_framework.renderers import JSONRenderer
from tqdm import tqdm

from core.aws import defaults
from theshow.serializers import OfficeSerializer

from .bake_base import BaseBakeCommand


class Command(BaseBakeCommand, BaseCommand):
    help = 'Bakes out context for an election.'

    def bake_federal_page(self, election_day, options):
        """ TK. """
        pass

    def bake_state_pages(self, election_day, options):
        """ TK. """
        pass

    def bake_federal_executive_race_page(self, election_day, options):
        """ TK. """
        pass

    def bake_state_executive_race_pages(self, election_day, options):
        elections = self.fetch_state_executive_race_elex(election_day)
        print('> >> State executive races:')
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
            self.bake(
                key,
                serialized_data,
                'application/json',
                production=options['production']
            )

    def bake_federal_body_pages(self, election_day, options):
        pass

    def bake_state_body_pages(self, election_day, options):
        pass
