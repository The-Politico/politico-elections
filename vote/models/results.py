from django.db import models
from core.models import UUIDBase
from election.models import Candidate, BallotAnswer, Election, BallotMeasure
from geography.models import Division


class BaseResult(UUIDBase):
    election = models.ForeignKey(Election)
    candidate = models.ForeignKey(Candidate, null=True)
    division = models.ForeignKey(Division)
    count = models.PositiveIntegerField()
    pct = models.DecimalField(decimal_places=3, max_digits=5)
    total = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Votes(BaseResult):
    ballot_answer = models.ForeignKey(BallotAnswer, null=True)
    winning = models.BooleanField(default=False)


class ElectoralVotes(BaseResult):
    winning = models.BooleanField(default=False)


class Delegates(BaseResult):
    superdelegates = models.BooleanField(default=False)


class APElectionMeta(UUIDBase):
    election = models.ForeignKey(Election, null=True)
    ballot_measure = models.ForeignKey(BallotMeasure, null=True)
    ap_election_id = models.CharField(max_length=10)
    called = models.BooleanField(default=False)
    tabulated = models.BooleanField(default=False)
    override_ap_call = models.BooleanField(default=False)
    override_ap_votes = models.BooleanField(default=False)
    precincts_reporting = models.PositiveIntegerField(null=True)
    precincts_total = models.PositiveIntegerField(null=True)
    precincts_reporting_pct = models.DecimalField(max_digits=5, decimal_places=3, null=True)