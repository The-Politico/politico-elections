import os

from django.template.loader import render_to_string
from tqdm import tqdm

from core.aws import defaults
from theshow.utils.bake.fetch import FetchMethods
from theshow.views import SpecialElectionPageExport


class SpecialElection(FetchMethods):

    def bake_special_election_pages(self, options):
        divisions = self.fetch_special_elections()

        for division in tqdm(divisions):
            context = {}
            context = SpecialElectionPageExport.build_context(
                election_datestring=self.ELECTION_DAY.__str__(),
                state_slug=division.slug,
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
                SpecialElectionPageExport.template_name,
                context
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                self.ELECTION_DAY.cycle.slug,
                division.slug,
                'special-election',
                self.ELECTION_DAY.special_election_datestring(),
                'index.html'
            )
            self.bake(
                key,
                template_string,
                content_type='text/html',
                production=options['production']
            )

    def handle(self, *args, **options):
        super(SpecialElection, self).handle(*args, **options)
        print('> >> Special elections:')
        self.bake_special_election_pages(options)
