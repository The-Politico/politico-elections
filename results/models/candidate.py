from django.db import models

from .base import LabelBase
from .election_meta import BallotMeasure, Party, Race


class Person(LabelBase):
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=10, null=True)

    def save(self, *args, **kwargs):
        self.label = '{0}{1}{2}'.format(
            self.first_name,
            '{0}'.format(
                ' ' + self.middle_name + ' ' if self.middle_name else ' '
            ),
            self.last_name
        )
        self.short_label = self.last_name
        super(Person, self).save(*args, **kwargs)


class Candidate(models.Model):
    person = models.ForeignKey(Person)
    party = models.ForeignKey(Party)
    race = models.ForeignKey(Race)
    ap_candidate_id = models.CharField(max_length=255)
    aggregable = models.BooleanField(default=True)

    def __str__(self):
        return self.person.label


class BallotAnswer(LabelBase):
    answer = models.TextField()
    ballot_measure = models.ForeignKey(BallotMeasure)
