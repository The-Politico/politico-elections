from django.contrib.postgres.fields import JSONField
from django.db import models

from .base import EffectiveDateBase, LabelBase, NameBase, SelfRelatedBase


class DivisionLevel(NameBase, SelfRelatedBase):
    """
    Level of government or administration at which a division exists.

    For example, federal, state, district, county, precinct, municipal.
    """
    pass


class Division(LabelBase, SelfRelatedBase, EffectiveDateBase):
    """
    A political or administrative geography.

    For example, a particular state, county, district, precinct or
    municipality.
    """
    level = models.ForeignKey(DivisionLevel)

    code = models.CharField(
        max_length=200,
        help_text="Code representing a geography: FIPS code for states and \
        counties, district number for districts, precinct number for \
        precincts, etc."
    )
    code_components = JSONField(
        blank=True,
        null=True,
        help_text="Component parts of code"
    )
