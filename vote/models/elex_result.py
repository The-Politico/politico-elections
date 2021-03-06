from django.db import models
from postgres_copy import CopyManager


class ResultRun(models.Model):
    """A time we hit the AP election API."""
    run_time = models.DateTimeField(auto_now=True)


class ElexResult(models.Model):
    """Bulk store of AP election API response."""
    elexid = models.CharField(max_length=80)
    raceid = models.CharField(max_length=5, null=True)
    racetype = models.TextField(null=True)
    racetypeid = models.CharField(max_length=1, null=True)
    ballotorder = models.PositiveSmallIntegerField(null=True)
    candidateid = models.TextField(null=True)
    description = models.TextField(null=True)
    delegatecount = models.IntegerField(null=True)
    electiondate = models.DateField(null=True)
    electtotal = models.PositiveSmallIntegerField(null=True)
    electwon = models.PositiveSmallIntegerField(null=True)
    fipscode = models.CharField(max_length=5, null=True)
    first = models.TextField(null=True)
    incumbent = models.BooleanField(default=False)
    initialization_data = models.BooleanField(default=False)
    is_ballot_measure = models.BooleanField(default=False)
    last = models.TextField(null=True)
    lastupdated = models.DateTimeField(null=True)
    level = models.TextField(null=True)
    national = models.BooleanField(default=False)
    officeid = models.CharField(max_length=1, null=True)
    officename = models.TextField(null=True)
    party = models.CharField(max_length=3, null=True)
    polid = models.TextField(null=True)
    polnum = models.TextField(null=True)
    precinctsreporting = models.PositiveSmallIntegerField(null=True)
    precinctsreportingpct = models.DecimalField(
        max_digits=7, decimal_places=6, null=True)
    precinctstotal = models.PositiveSmallIntegerField(null=True)
    resultrun = models.ForeignKey(ResultRun)
    reportingunitid = models.TextField(null=True)
    reportingunitname = models.TextField(null=True)
    runoff = models.BooleanField(default=False)
    seatname = models.TextField(null=True)
    seatnum = models.PositiveSmallIntegerField(null=True)
    statename = models.TextField(null=True)
    statepostal = models.CharField(max_length=2, null=True)
    test = models.BooleanField(default=False)
    uncontested = models.BooleanField(default=False)
    votecount = models.PositiveIntegerField(null=True)
    votepct = models.DecimalField(max_digits=7, decimal_places=6, null=True)
    winner = models.BooleanField(default=False)
    objects = CopyManager()
