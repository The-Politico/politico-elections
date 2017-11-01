from django.db import models

from core.models import UUIDBase
from election.models import (BallotAnswer, BallotMeasure, CandidateElection,
                             Election)
from geography.models import Division


class BaseResult(UUIDBase):
    """
    UUID
    """
    division = models.ForeignKey(Division)
    count = models.PositiveIntegerField()
    pct = models.DecimalField(decimal_places=3, max_digits=5)
    total = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Votes(BaseResult):
    candidate_election = models.ForeignKey(
        CandidateElection, null=True, blank=True, related_name="votes"
    )
    ballot_answer = models.ForeignKey(BallotAnswer, null=True, blank=True)
    winning = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.candidate_election.candidate.person.last_name,
            self.candidate_election.election,
            self.division
        )


class ElectoralVotes(BaseResult):
    candidate_election = models.ForeignKey(
        CandidateElection,
        null=True,
        blank=True,
        related_name="electoral_votes"
    )
    winning = models.BooleanField(default=False)


class Delegates(BaseResult):
    candidate_election = models.ForeignKey(
        CandidateElection, null=True, blank=True, related_name="delegates"
    )
    superdelegates = models.BooleanField(default=False)


class APElectionMeta(UUIDBase):
    """
    UUID
    """
    election = models.OneToOneField(
        Election,
        related_name='meta',
        on_delete=models.CASCADE,
        null=True, blank=True)
    ballot_measure = models.OneToOneField(
        BallotMeasure,
        related_name='meta',
        on_delete=models.CASCADE,
        null=True, blank=True)
    ap_election_id = models.CharField(max_length=10)
    called = models.BooleanField(default=False)
    tabulated = models.BooleanField(default=False)
    override_ap_call = models.BooleanField(default=False)
    override_ap_votes = models.BooleanField(default=False)
    precincts_reporting = models.PositiveIntegerField(null=True, blank=True)
    precincts_total = models.PositiveIntegerField(null=True, blank=True)
    precincts_reporting_pct = models.DecimalField(
        max_digits=5, decimal_places=3, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "AP election meta data"
