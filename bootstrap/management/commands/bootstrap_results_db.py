import json
import subprocess

from django.core.management.base import BaseCommand
from tqdm import tqdm

import election.models as election
import server_config
import vote.models as vote


class Command(BaseCommand):
    help = (
        'Ingests master results JSON file from Elex and updates the results '
        'models in Django.'
    )

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        writefile = open('master.json', 'w')
        elex_args = ['elex', 'results', options['election_date']]
        elex_args.extend(server_config.ELEX_FLAGS)
        subprocess.run(elex_args, stdout=writefile)

        with open('master.json') as f:
            data = json.load(f)

        for result in tqdm(data):
            if result['is_ballot_measure']:
                continue

            ap_meta = vote.APElectionMeta.objects.get(
                ap_election_id=result['raceid'],
                election__division__name=result['statename']
            )

            id_components = result['id'].split('-')
            candidate_id = '{0}-{1}'.format(
                id_components[1],
                id_components[2]
            )
            candidate = election.Candidate.objects.get(
                ap_candidate_id=candidate_id
            )

            candidate_election = election.CandidateElection.objects.get(
                election=ap_meta.election,
                candidate=candidate
            )

            kwargs = {
                'candidate_election': candidate_election,
                'division': ap_meta.election.division
            }

            if not ap_meta.override_ap_votes:
                kwargs['count'] = result['votecount']
                kwargs['pct'] = result['votepct']

            if not ap_meta.override_ap_call:
                kwargs['winning'] = result['winner']

            vote.Votes.objects.update_or_create(**kwargs)
