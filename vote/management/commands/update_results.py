import json
import election.models as election
import geography.models as geography
import vote.models as vote

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'ingests master JSON file to update results models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help="force update to run"
        )

    def handle(self, *args, **options):
        with open('master.json') as f:
            data = json.load(f)

        for result in data:
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

            vote.Votes.objects.update_or_create(
                election=ap_meta.election,
                candidate=candidate,
                division=ap_meta.election.division,
                count=result['votecount'],
                pct=result['votepct'],
                total=result['votecount'],
                winning=result['winner']
            )
