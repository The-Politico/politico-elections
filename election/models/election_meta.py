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
    ap_code = models.CharField(max_length=3, unique=True)
    aggregate_candidates = models.BooleanField(default=True)

<<<<<<< Updated upstream
=======
    # {ap_code}

    def __str__(self):
        if self.label:
            return self.label
        return self.name

>>>>>>> Stashed changes
    class Meta:
        verbose_name_plural = 'Parties'


class BallotMeasure(LabelBase):
    """
    """
    question = models.TextField()
    division = models.ForeignKey(Division, related_name='ballot_measures')
    number = models.CharField(max_length=3)
    election_day = models.ForeignKey(
        'ElectionDay', related_name='ballot_measures')

    # division_cycle_ballot_measure-{number}


class ElectionDay(UUIDBase):
    """
    election_date = 2018-11-08
    """
    date = models.DateField(unique=True)
    cycle = models.ForeignKey(ElectionCycle, related_name='elections_days')

    # {cycle}-{date}

    def __str__(self):
        return str(self.date)


class Race(LabelBase):
    office = models.ForeignKey(Office, related_name='races')
    cycle = models.ForeignKey(ElectionCycle, related_name='races')

    def save(self, *args, **kwargs):
        # officeslug_race-{cycle}

        name_label = '{0} {1}'.format(
            self.cycle.name,
            self.office.label
        )

        self.label = name_label
        self.name = name_label

        super(Race, self).save(*args, **kwargs)


class Election(UUIDBase):
    election_type = models.ForeignKey(ElectionType, related_name='elections')
    race = models.ForeignKey('Race', related_name='elections')
    party = models.ForeignKey(Party, null=True, blank=True)
    election_day = models.ForeignKey(ElectionDay, related_name='elections')
    division = models.ForeignKey(Division, related_name='elections')

    def __str__(self):
        # raceslug_election-{election_day}-{party?}

        base = '{0}, {1}, {2}'.format(
            self.race.office.label,
            self.election_type.label,
            self.election_day.date
        )

        if self.party:
            return '{0} {1}'.format(self.party.label, base)
        else:
            return base
