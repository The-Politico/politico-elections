from django.db import models

from .base import LabelBase
from .geography import Geography


class ElectionCycle(LabelBase):
    """
    e.g. "2016"
    """
    pass


class RaceType(LabelBase):
    """
    e.g. "General", "Primary"
    """
    pass


class Office(LabelBase):
    """
    label = 'Senate'
    office_level = 0
    """
    FEDERAL = 0
    STATE = 1
    MUNICIPAL = 2

    LEVEL_CHOICES = (
        (FEDERAL, 'Federal'),
        (STATE, 'State'),
        (MUNICIPAL, 'Municipal'),
    )

    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)


class Seat(LabelBase):
    """
    e.g. "Senator", "Governor"
    """
    geography = models.ForeignKey(Geography)
    office = models.ForeignKey(Office)


class Party(LabelBase):
    """
    label = "Republican"
    ap_code = "gop"
    short_label = "GOP"
    """
    ap_code = models.CharField(max_length=3)
    aggregate_candidates = models.BooleanField(default=True)


class Election(models.Model):
    """
    election_date = 2018-11-08
    """
    date = models.DateField()
    cycle = models.ForeignKey(ElectionCycle)

    def __str__(self):
        return self.election_date


class BallotMeasure(LabelBase):
    """
    """
    question = models.TextField()
    geography = models.ForeignKey(Geography)
    election = models.ForeignKey(Election)


class Race(LabelBase):
    election = models.ForeignKey(Election)
    race_type = models.ForeignKey(RaceType)
    seat = models.ForeignKey(Seat)
    party = models.ForeignKey(Party, null=True)

    def save(self, *args, **kwargs):
        base = '{0} {1} {2}, {3}'.format(
            self.seat.geography.label,
            self.seat.office.label,
            self.race_type.label,
            self.election.date
        )

        if self.party:
            self.label = '{0} {1}'.format(self.party.label, base)
        else:
            self.label = base

        super(Race, self).save(*args, **kwargs)
