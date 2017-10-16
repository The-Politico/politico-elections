from django.db import models

from core.models import LabelBase, NameBase, UUIDBase
from entity.models import Office
from geography.models import Division


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
    election_day = models.ForeignKey('ElectionDay')


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
        base = '{0}, {1}, {2}'.format(
            self.race.office.label,
            self.election_type.label,
            self.election_day.date
        )

        if self.party:
            self.label = '{0} {1}'.format(self.party.label, base)
            self.name = '{0} {1}'.format(self.party.label, base)
        else:
            self.label = base
            self.name = base

        super(Election, self).save(*args, **kwargs)


class Race(LabelBase):
    office = models.ForeignKey(Office)
    cycle = models.ForeignKey(ElectionCycle)

    def save(self, *args, **kwargs):
        name_label = '{0} {1}'.format(
            self.cycle.name,
            self.office.label
        )

        self.label = name_label
        self.name = name_label

        super(Race, self).save(*args, **kwargs)

