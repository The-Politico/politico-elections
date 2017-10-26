from django.db import models

from core.models import LabelBase, UIDBase, UUIDBase
from entity.models import Person

from .election_meta import BallotMeasure, Election, Party, Race


class Candidate(UIDBase):
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

    def save(self, *args, **kwargs):
        """
        uid: {person.uid}_candidate:{party.uid}-{cycle.ap_code}
        """
        self.uid = '{}_candidate:{}-{}'.format(
            self.person.uid,
            self.party.uid,
            self.race.cycle.uid
        )
        super(Candidate, self).save(*args, **kwargs)

    def __str__(self):
        return self.person.name


class BallotAnswer(UUIDBase, LabelBase):
    answer = models.TextField()
    winner = models.BooleanField(default=False)
    ballot_measure = models.ForeignKey(BallotMeasure)
