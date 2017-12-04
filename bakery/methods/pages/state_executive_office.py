import os

from django.template.loader import render_to_string
from tqdm import tqdm

from bakery.methods.fetch import FetchMethods
from core.aws import defaults
from theshow.views import StateExecutiveRacePageExport


class StateExecutiveOffice(FetchMethods):

    def bake_state_executive_race_pages(self, options):
        elections = self.fetch_state_executive_office_elections()

        for election in tqdm(elections):
            context = StateExecutiveRacePageExport.build_context(
                election_datestring=election.election_day.__str__(),
                state_slug=election.division.slug,
                office_slug=election.race.office.slug,
            )
            context['hash'] = options['hash']
            context['domain'] = defaults.DOMAIN[
                'production' if options['production'] else 'staging'
            ]
            context['root_path'] = defaults.ROOT_PATH
            context['data_domain'] = defaults.DATA_DOMAIN[
                'production' if options['production'] else 'staging'
            ]
            template_string = render_to_string(
                StateExecutiveRacePageExport.template_name,
                context
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                self.ELECTION_DAY.cycle.slug,
                election.division.slug,
                election.race.office.slug.lower(),
                'index.html'
            )
            self.bake(
                key,
                template_string,
                content_type='text/html',
                production=options['production']
            )

    def handle(self, *args, **options):
        super(StateExecutiveOffice, self).handle(*args, **options)
        print('> >> State executive races:')
        self.bake_state_executive_race_pages(options)
