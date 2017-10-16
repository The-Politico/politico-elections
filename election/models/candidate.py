from django.db import models

from core.models import LabelBase
from entity.models import Person
from .election_meta import BallotMeasure, Party, Race


class Candidate(LabelBase):
    race = models.ForeignKey(Race)
    person = models.ForeignKey(Person)
    party = models.ForeignKey(Party)
    ap_candidate_id = models.CharField(max_length=255)
    aggregable = models.BooleanField(default=True)
    winner = models.BooleanField(default=False)
    incumbent = models.BooleanField(default=False)
    uncontested = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, null=True)
    image = models.URLField(null=True, blank=True)
    top_of_ticket = models.ForeignKey('self', null=True, related_name='ticket')

    def __str__(self):
        return self.person.label


class BallotAnswer(LabelBase):
    answer = models.TextField()
    winner = models.BooleanField(default=False)
    ballot_measure = models.ForeignKey(BallotMeasure)
