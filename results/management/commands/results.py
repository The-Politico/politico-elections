import subprocess

from django.core.management.base import BaseCommand, CommandError
from results.models import ElexResult

class Command(BaseCommand):
    help = 'gets results for a particular election date'

    def add_arguments(self, parser):
        parser.add_argument('election_date', type=str)

    def handle(self, *args, **options):
        with open('test.csv') as f:
            subprocess.run(['elex', 'results', options['election_date']], stdout=f)

        ElexResult.objects.from_csv(
            'test.csv',
            dict(
                id='id',
                raceid='raceid',
                racetype='racetype',
                racetypeid='racetypeid',
                ballotorder='ballotorder',
                candidateid='candidateid',
                description='description',
                delegatecount='delegatecount',
                electiondate='electiondate',
                electtotal='electtotal',
                electwon='electwon',
                fipscode='fipscode',
                first='first',
                incumbent='incumbent',
                initialization_data='initialization_data',
                is_ballot_measure='is_ballot_measure',
                last='last',
                lastupdated='lastupdated',
                level='level',
                national='national',
                officeid='officeid',
                officename='officename',
                party='party',
                polid='polid',
                polnum='polnum',
                precinctsreporting='precinctsreporting',
                precinctsreportingpct='precinctsreportingpct',
                precinctstotal='precinctstotal',
                reportingunitid='reportingunitid',
                reportingunitname='reportingunitname',
                runoff='runoff',
                seatname='seatname',
                seatnum='seatnum',
                statename='statename',
                statepostal='statepostal',
                test='test',
                uncontested='uncontested',
                votecount='votecount',
                votepct='votepct',
                winner='winner',
            )
        )
