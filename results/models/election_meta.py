from django.db import models
from .base import SlugModel
from .geography import Geography


class ElectionCycle(SlugModel):
    """
    e.g. "2016"
    """
    pass


class ElectionType(SlugModel):
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

    office_level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)


class Seat(SlugModel):
    """
    e.g. "Senator", "Governor"
    """
    seat_geography = models.ForeignKey(Geography)
    seat_office = models.ForeignKey(Office)


class Party(SlugModel):
    """
    label = "Republican"
    ap_code = "gop"
    short_label = "GOP"
    """
    ap_code = models.CharField(max_length=3)


class Election(models.Model):
    """
    election_date = 2018-11-08
    """
    election_date = models.DateField()
    election_cycle = models.ForeignKey(ElectionCycle)

    def __str__(self):
        return self.election_date


class Race(models.Model):
    election = models.ForeignKey(Election)
    election_type = models.ForeignKey(ElectionType)
    seat = models.ForeignKey(Seat)
    party = models.ForeignKey(Party, null=True)

    def __str__(self):
        base = '{0} {1} {2}, {3}'.format(
            self.seat.seat_geography.label,
            self.seat.seat_office.label,
            self.election_type.label,
            self.election.election_date
        )

        if self.party:
            return '{0} {1}'.format(self.party, base)
        else:
            return base
