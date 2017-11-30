import os

from rest_framework.renderers import JSONRenderer
from tqdm import tqdm

from core.aws import defaults
from theshow.serializers import SpecialElectionSerializer
from theshow.utils.bake.fetch import FetchMethods


class SpecialElection(FetchMethods):

    def bake_special_election_context(self, options):
        divisions = self.fetch_special_elections()

        for division in tqdm(divisions):
            serialized_data = JSONRenderer().render(
                SpecialElectionSerializer(division, context={
                    'election_date': self.ELECTION_DAY.date
                }).data
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                self.ELECTION_DAY.cycle.slug,
                division.slug,
                'special-election',
                self.ELECTION_DAY.special_election_datestring(),
                'context.json'
            )
            self.bake(
                key,
                serialized_data,
                'application/json',
                production=options['production']
            )

    def handle(self, *args, **options):
        super(SpecialElection, self).handle(*args, **options)
        print('> >> State executive races:')
        self.bake_special_election_context(options)
