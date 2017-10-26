from django.db import models

from core.models import LabelBase
from entity.models import Person

from .election_meta import BallotMeasure, Election, Party, Race


class Candidate(LabelBase):
    """
    uuid
    slug
    name
    label
    short_label
    """
    race = models.ForeignKey(Race, related_name='candidates')
    elections = models.ManyToManyField(Election, related_name='candidates')
    person = models.ForeignKey(Person, related_name='candidacies')
    party = models.ForeignKey(Party, related_name='candidates')
    ap_candidate_id = models.CharField(max_length=255)
    aggregable = models.BooleanField(default=True)
    winner = models.BooleanField(default=False)
    incumbent = models.BooleanField(default=False)
    uncontested = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    top_of_ticket = models.ForeignKey(
        'self', null=True, blank=True, related_name='ticket')

    def __str__(self):
        return self.person.label


class BallotAnswer(LabelBase):
    """
    uuid
    slug
    name
    label
    short_label
    """
    answer = models.TextField()
    winner = models.BooleanField(default=False)
    ballot_measure = models.ForeignKey(BallotMeasure)
