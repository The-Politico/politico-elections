from django.db import models
from .base import SlugModel
from .geography import Geography


class ElectionCycle(SlugModel):
    """
    e.g. "2016"
    """
    pass


class RaceType(SlugModel):
    """
    e.g. "General", "Primary"
    """
    pass


class Office(SlugModel):
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


class Seat(SlugModel):
    """
    e.g. "Senator", "Governor"
    """
    geography = models.ForeignKey(Geography)
    office = models.ForeignKey(Office)


class Party(SlugModel):
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


class BallotMeasure(SlugModel):
    """
    """
    question = models.TextField()
    geography = models.ForeignKey(Geography)
    election = models.ForeignKey(Election)
    precincts_reporting = models.PositiveIntegerField(null=True)
    precincts_total = models.PositiveIntegerField(null=True)
    precincts_reporting_pct = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    called = models.BooleanField(default=False)
    tabulated = models.BooleanField(default=False)


class Race(SlugModel):
    election = models.ForeignKey(Election)
    race_type = models.ForeignKey(RaceType)
    seat = models.ForeignKey(Seat)
    party = models.ForeignKey(Party, null=True)
    ap_race_id = models.CharField(max_length=10)
    precincts_reporting = models.PositiveIntegerField(null=True)
    precincts_total = models.PositiveIntegerField(null=True)
    precincts_reporting_pct = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    called = models.BooleanField(default=False)
    tabulated = models.BooleanField(default=False)

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
