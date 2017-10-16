from django.db import models
<<<<<<< Updated upstream

from .candidate import BallotMeasure, Candidate
from .base import UUIDBase
from .candidate import Candidate, BallotAnswer
from .election_meta import Election
from .division import Divison


class BaseResult(UUIDBase):
    election = models.ForeignKey(Election)
    candidate = models.ForeignKey(Candidate, null=True)
    division = models.ForeignKey(Divison)
    count = models.PositiveIntegerField()
    pct = models.DecimalField(decimal_places=3, max_digits=5)
    total = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class Votes(BaseResult):
    ballot_answer = models.ForeignKey(BallotAnswer, null=True)
    winning = models.BooleanField(default=False)


class ElectoralVotes(BaseResult):
    winning = models.BooleanField(default=False)


class Delegates(BaseResult):
    superdelegates = models.BooleanField(default=False)