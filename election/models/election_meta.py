from django.db import models

from core.models import LabelBase, NameBase, UUIDBase
from entity.models import Office
from geography.models import Division


class ElectionCycle(NameBase):
    """
    e.g. "2016"

    uuid
    slug
    name
    """
    pass


class ElectionType(LabelBase):
    """
    e.g. "General", "Primary"

    uuid
    slug
    name
    label
    short_label
    """
    ap_code = models.CharField(max_length=1)


class Party(LabelBase):
    """
    label = "Republican"
    ap_code = "gop"
    short_label = "GOP"

    uuid
    slug
    name
    label
    short_label
    """
    ap_code = models.CharField(max_length=3, unique=True)
    aggregate_candidates = models.BooleanField(default=True)

    def __str__(self):
        if self.label:
            return self.label
        return self.name

    class Meta:
        verbose_name_plural = 'Parties'


class BallotMeasure(LabelBase):
    """
    uuid
    slug
    name
    label
    short_label
    """
    question = models.TextField()
    division = models.ForeignKey(Division, related_name='ballot_measures')
    election_day = models.ForeignKey(
        'ElectionDay', related_name='ballot_measures')


class ElectionDay(UUIDBase):
    """
    election_date = 2018-11-08
    """
    date = models.DateField(unique=True)
    cycle = models.ForeignKey(ElectionCycle, related_name='elections_days')

    def __str__(self):
        return str(self.date)


class Race(LabelBase):
    """
    uuid
    slug
    name
    label
    short_label
    """
    office = models.ForeignKey(Office, related_name='races')
    cycle = models.ForeignKey(ElectionCycle, related_name='races')

    def save(self, *args, **kwargs):
        name_label = '{0} {1}'.format(
            self.cycle.name,
            self.office.label
        )

        self.label = name_label
        self.name = name_label

        super(Race, self).save(*args, **kwargs)


class Election(UUIDBase):
    """
    UUID
    """
    election_type = models.ForeignKey(ElectionType, related_name='elections')
    race = models.ForeignKey('Race', related_name='elections')
    party = models.ForeignKey(Party, null=True, blank=True)
    election_day = models.ForeignKey(ElectionDay, related_name='elections')
    division = models.ForeignKey(Division, related_name='elections')

    def __str__(self):
        base = '{0}, {1}, {2}'.format(
            self.race.office.label,
            self.election_type.label,
            self.election_day.date
        )

        if self.party:
            return '{0} {1}'.format(self.party.label, base)
        else:
            return base
