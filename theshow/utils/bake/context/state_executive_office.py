import os

from rest_framework.renderers import JSONRenderer
from tqdm import tqdm

from core.aws import defaults
from theshow.serializers import OfficeSerializer
from theshow.utils.bake.fetch import FetchMethods


class StateExecutiveOffice(FetchMethods):

    def bake_state_executive_race_context(self, options):
        elections = self.fetch_state_executive_office_elections()

        for election in tqdm(elections):
            serialized_data = JSONRenderer().render(
                OfficeSerializer(election.race.office, context={
                    'election_date': self.ELECTION_DAY.date
                }).data
            )
            key = os.path.join(
                defaults.ROOT_PATH,
                self.ELECTION_DAY.cycle.slug,
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

    def handle(self, *args, **options):
        super(StateExecutiveOffice, self).handle(*args, **options)
        print('> >> State executive races:')
        self.bake_state_executive_race_context(options)
