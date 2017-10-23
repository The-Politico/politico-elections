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

    class Meta:
        verbose_name_plural = 'Parties'


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
        return str(self.date)


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


class Election(LabelBase):
    election_type = models.ForeignKey(ElectionType)
    race = models.ForeignKey('Race')
    party = models.ForeignKey(Party, null=True, blank=True)
    election_day = models.ForeignKey(ElectionDay)
    division = models.ForeignKey(Division)

    def save(self, *args, **kwargs):
        base = '{0} {1}'.format(
            self.race.cycle.name,
            self.race.office.label
        )

        if self.election_type.label != 'General':
            if self.party:
                extra_info = '{0} {1}'.format(
                    self.party.label,
                    self.election_type.label
                )
            else:
                extra_info = self.election_type.label

            self.label = '{0} {1}'.format(
                base,
                extra_info
            )
            self.name = '{0} {1}'.format(
                base,
                extra_info
            )
        else: 
            self.label = base
            self.name = base

        super(Election, self).save(*args, **kwargs)
