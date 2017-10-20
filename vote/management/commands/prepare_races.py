import json

from django.core.management.base import BaseCommand, CommandError
from election.models import Election, ElectionCycle
from uuslug import slugify

class Command(BaseCommand):
    help = 'finds race ids necessary for pages'

    def serialize_cycle(self, cycle):
        """
        /election-results/cycle/
        """
        elections = Election.objects.filter(
            race__cycle__name=cycle
        )

        self._write_to_json(elections, cycle)

    def serialize_federal_body(self, body, elections):
        """
        /election-results/cycle/senate/
        /election-results/cycle/house/
        """
        body_elections = elections.filter(
            race__office__body__slug=body
        )

        self._write_to_json(body_elections, body)

    def serialize_federal_exec(self, office, elections):
        """
        /election-results/cycle/president/
        """
        office_elections = elections.filter(
            race__office__slug=office
        )

        self._write_to_json(office_elections, office)

    def serialize_state(self, state, elections):
        """
        /election-results/cycle/state/
        """
        state_elections = elections.filter(
            division__slug=state
        )

        self._write_to_json(state_elections, state)

    def serialize_state_body(self, state, body, elections):
        """
        /election-results/cycle/senate/state/
        /election-results/cycle/house/state/
        /election-results/cycle/state/senate/
        /election-results/cycle/state/house/
        """
        state_federal_body_elections = elections.filter(
            division__slug=state,
            race__office__body__slug=body
        )   

        key = '{0}-{1}'.format(body, state)
        self._write_to_json(state_federal_body_elections, key)

    def serialize_state_exec(self, state, office, elections):
        """
        /election-results/cycle/president/state/
        /election-results/cycle/state/governor
        """
        state_office_elections = elections.filter(
            division__slug=state,
            race__office__slug=office
        )

        key = '{0}-{1}'.format(state, office)
        self._write_to_json(state_office_elections, key)


    def _write_to_json(self, elections, key):
        ids = []
        for election in elections:
            meta = election.apelectionmeta_set.all()
            if (len(meta) > 0):
                ids.append(meta[0].ap_election_id)

        with open('output/elections/{0}.json'.format(key), 'w') as f:
            json.dump(ids, f)


    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        latest_cycle = ElectionCycle.objects.get(name='2018').name
        self.serialize_cycle(latest_cycle)

        elections = Election.objects.filter(
            election_day__date=options['election_date'],
        )

        bodies = set(elections.filter(
            race__office__body__name__isnull=False,
        ).values_list('race__office__body__slug', flat=True))
        states = set(elections.filter(
            race__office__division__level__name='state',
        ).values_list('division__slug', flat=True))
        exec_offices = set(elections.filter(
            race__office__body__isnull=True
        ).values_list('race__office__slug', flat=True))

        for body in bodies:
            self.serialize_federal_body(body, elections)

            for state in states:
                self.serialize_state_body(state, body, elections)

        for state in states:
            self.serialize_state(state, elections)

        for office in exec_offices:
            self.serialize_federal_exec(office, elections)

            for state in states:
                self.serialize_state_exec(state, office, elections)