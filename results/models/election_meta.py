from django.db import models

from .base import LabelBase, NameBase, UUIDBase
from .division import Division


class ElectionCycle(NameBase):
    """
    e.g. "2016"
    """
    pass


class ElectionType(LabelBase):
    """
    e.g. "General", "Primary"
    """
    ap_code = models.CharField(max_length=1)


class Body(LabelBase):
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


class Office(LabelBase):
    """
    e.g. "Senator", "Governor"
    """
    division = models.ForeignKey(Division)
    body = models.ForeignKey(Body, null=True)


class Party(LabelBase):
    """
    label = "Republican"
    ap_code = "gop"
    short_label = "GOP"
    """
    ap_code = models.CharField(max_length=3)
    aggregate_candidates = models.BooleanField(default=True)


class BallotMeasure(LabelBase):
    """
    """
    question = models.TextField()
    division = models.ForeignKey(Division)
    election = models.ForeignKey('Election')


class ElectionDay(UUIDBase):
    """
    election_date = 2018-11-08
    """
    date = models.DateField()
    cycle = models.ForeignKey(ElectionCycle)

    def __str__(self):
        return self.election_date


class Election(LabelBase):
    election_type = models.ForeignKey(ElectionType)
    race = models.ForeignKey('Race')
    party = models.ForeignKey(Party, null=True)
    election_day = models.ForeignKey(ElectionDay)
    division = models.ForeignKey(Division)

    def save(self, *args, **kwargs):
        base = '{0} {1} {2}, {3}'.format(
            self.division.label,
            self.race.office.body.label,
            self.election_type.label,
            self.election_day.date
        )

        if self.party:
            self.label = '{0} {1}'.format(self.party.label, base)
        else:
            self.label = base

        super(Election, self).save(*args, **kwargs)


class Race(LabelBase):
    office = models.ForeignKey(Office)
    cycle = models.ForeignKey(ElectionCycle)

    def save(self, *args, **kwargs):
        self.label = '{0} {1}'.format(
            self.cycle.label,
            self.office.label
        )

        super(Race, self).save(*args, **kwargs)


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

