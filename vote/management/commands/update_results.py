import json
import election.models as election
import geography.models as geography
import vote.models as vote

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'ingests master JSON file to update results models'

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

            if result['polid']:
                candidate_id = 'polid-{0}'.format(result['polid'])
            else:
                candidate_id = 'polnum-{0}'.format(result['polnum'])



            candidates = election.Candidate.objects.filter(
                ap_candidate_id=candidate_id
            )
            candidate = candidates[0]


            vote.Votes.objects.update_or_create(
                election=ap_meta.election,
                candidate=candidate,
                division=ap_meta.election.division,
                count=result['votecount'],
                pct=result['votepct'],
                total=result['votecount'],
                winning=result['winner']
            )