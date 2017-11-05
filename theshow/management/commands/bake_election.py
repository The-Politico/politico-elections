import os

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from tqdm import tqdm

from core.aws import defaults
from theshow.views import StateExecutiveRacePageExport

from .bake_base import BaseBakeCommand


class Command(BaseBakeCommand, BaseCommand):
    help = 'Bakes pages for an election.'

    def bake_federal_page(self, election_day):
        pass

    def bake_state_pages(self, election_day):
        pass

    def bake_federal_executive_race_page(self, election_day):
        pass

    def bake_state_executive_race_pages(self, election_day):
        elections = self.fetch_state_executive_race_elex(election_day)
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
            self.bake(
                key,
                template_string,
                content_type='text/html'
            )

    def bake_federal_body_pages(self, election_day):
        pass

    def bake_state_body_pages(self, election_day):
        pass
