from django.db import models
from uuslug import slugify, uuslug

from core.models import LabelBase, NameBase, SlugBase, UIDBase, UUIDBase
from entity.models import Office
from geography.models import Division


class ElectionCycle(UIDBase, SlugBase, NameBase):
    def save(self, *args, **kwargs):
        """
        uid: cycle:{year}
        """
        self.slug = slugify(self.name)
        self.uid = 'cycle:{}'.format(self.slug)
        super(ElectionCycle, self).save(*args, **kwargs)


class ElectionType(UIDBase, LabelBase):
    """
    e.g. "General", "Primary"

    uuid
    slug
    name
    label
    short_label
    """
    ap_code = models.CharField(max_length=1)

    def save(self, *args, **kwargs):
        """
        uid: electiontype:{name}
        """
        self.uid = 'electiontype:{}'.format(slugify(self.name))
        super(ElectionType, self).save(*args, **kwargs)


class Party(UIDBase, SlugBase, LabelBase):
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

    def save(self, *args, **kwargs):
        """
        uid: party:{apcode}
        """
        self.uid = 'party:{}'.format(slugify(self.ap_code))
        self.slug = self.name
        super(Party, self).save(*args, **kwargs)


class ElectionDay(UIDBase, SlugBase):
    """
    election_date = 2018-11-08
    """
    date = models.DateField(unique=True)
    cycle = models.ForeignKey(ElectionCycle, related_name='elections_days')

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        """
        uid: {cycle.uid}_date:{date}
        """
        self.uid = '{}_date:{}'.format(
            self.cycle.uid,
            self.date
        )
        self.slug = '{}'.format(self.date)
        super(ElectionDay, self).save(*args, **kwargs)


class BallotMeasure(UIDBase, LabelBase):
    """
    """
    question = models.TextField()
    division = models.ForeignKey(Division, related_name='ballot_measures')
    number = models.CharField(max_length=3)
    election_day = models.ForeignKey(
        'ElectionDay', related_name='ballot_measures')

    def save(self, *args, **kwargs):
        """
        uid: division_cycle_ballotmeasure:{number}
        """
        self.uid = '{}_{}_ballotmeasure:{}'.format(
            self.division.uid,
            self.election_day.uid,
            self.number
        )
        super(BallotMeasure, self).save(*args, **kwargs)


class Race(UIDBase, SlugBase, LabelBase):
    office = models.ForeignKey(Office, related_name='races')
    cycle = models.ForeignKey(ElectionCycle, related_name='races')

    def save(self, *args, **kwargs):
        """
        uid: {office.uid}_{cycle.uid}_race
        """
        self.uid = '{}_{}_race'.format(
            self.office.uid,
            self.cycle.uid
        )

        name_label = '{0} {1}'.format(
            self.cycle.name,
            self.office.label
        )

        self.label = name_label
        self.name = name_label
        if not self.slug:
            self.slug = uuslug(
                name_label,
                instance=self,
                max_length=100,
                separator='-',
                start_no=2
            )

        super(Race, self).save(*args, **kwargs)


class Election(UIDBase):
    election_type = models.ForeignKey(ElectionType, related_name='elections')
    candidates = models.ManyToManyField(
        'Candidate', through='CandidateElection')
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

    def save(self, *args, **kwargs):
        """
        uid: {race.uid}_election:{election_day}-{party}
        """
        if self.party:
            self.uid = '{}_election:{}-{}'.format(
                self.race.uid,
                self.election_day.date,
                slugify(self.party.ap_code)
            )
        else:
            self.uid = '{}_election:{}'.format(
                self.race.uid,
                self.election_day.date
            )
        super(Election, self).save(*args, **kwargs)

    def update_or_create_candidate(
        self, candidate, aggregable=True, uncontested=False
    ):
        candidate_election, c = CandidateElection.objects.update_or_create(
            candidate=candidate,
            election=self,
            defaults={
                'aggregable': aggregable,
                'uncontested': uncontested
            }
        )

        return candidate_election

    def delete_candidate(self, candidate):
        CandidateElection.objects.filter(
            candidate=candidate,
            election=self
        ).delete()

    def get_candidates(self):
        candidate_elections = CandidateElection.objects.filter(
            election=self
        )

        return [ce.candidate for ce in candidate_elections]

    def get_candidate_election(self, candidate):
        return CandidateElection.objects.get(
            candidate=candidate,
            election=self
        )

    def get_candidate_votes(self, candidate):
        candidate_election = CandidateElection.objects.get(
            candidate=candidate,
            election=self
        )

        return candidate_election.votes.all()

    def get_votes(self):
        candidate_elections = CandidateElection.objects.filter(
            election=self
        )

        votes = None
        for ce in candidate_elections:
            votes = votes | ce.votes.all()

        return votes

    def get_candidate_electoral_votes(self, candidate):
        candidate_election = CandidateElection.objects.get(
            candidate=candidate,
            election=self
        )

        return candidate_election.electoral_votes.all()

    def get_electoral_votes(self):
        candidate_elections = CandidateElection.objects.filter(
            election=self
        )

        electoral_votes = None
        for ce in candidate_elections:
            electoral_votes = electoral_votes | ce.electoral_votes.all()

        return electoral_votes

    def get_candidate_delegates(self, candidate):
        candidate_election = CandidateElection.objects.get(
            candidate=candidate,
            election=self
        )

        return candidate_election.delegates.all()

    def get_delegates(self):
        candidate_elections = CandidateElection.objects.filter(
            election=self
        )

        delegates = None
        for ce in candidate_elections:
            delegates = delegates | ce.delegates.all()

        return delegates


class CandidateElection(UUIDBase):
    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
        related_name='candidate_elections'
    )
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
        related_name='candidate_elections'
    )
    aggregable = models.BooleanField(default=True)
    uncontested = models.BooleanField(default=False)

    class Meta:
        unique_together = (('candidate', 'election'),)
