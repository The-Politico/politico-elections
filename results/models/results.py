from django.db import models

from .candidate import BallotMeasure, Candidate
from .geography import Geography


class Result(models.Model):
    candidate = models.ForeignKey(Candidate, null=True)
    ballot_measure = models.ForeignKey(BallotMeasure, null=True)
    vote_count = models.PositiveIntegerField()
    vote_pct = models.DecimalField(decimal_places=3, max_digits=5)
    total_votes = models.PositiveIntegerField()
    geography = models.ForeignKey(Geography)
