from django.db import models
from core.models import LabelBase
from geography.models import Division


class Body(LabelBase):
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


class Office(LabelBase):
    """
    e.g. "Senator", "Governor"
    """
    division = models.ForeignKey(Division)
    body = models.ForeignKey(Body, null=True)