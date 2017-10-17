from django.db import models

from core.models import LabelBase, SelfRelatedBase
from geography.models import Division


class Jurisdiction(LabelBase, SelfRelatedBase):
    """
    A Jurisdiction represents a logical unit of governance, comprising of
    a collection of legislative bodies, administrative offices or public
    services.

    For example: the United States Federal Government, the Government
    of the District of Columbia, Columbia Missouri City Government, etc.
    """
    division = models.ForeignKey(Division, null=True)


class Body(LabelBase, SelfRelatedBase):
    """
    A body represents a collection of offices or individuals organized around a
    common government or public service function.

    For example: the U.S. Senate, Florida House of Representatives, Columbia
    City Council, etc.

    name = 'Senate'
    label = 'U.S. Senate'
    """
    jurisdiction = models.ForeignKey(Jurisdiction)

    class Meta:
        verbose_name_plural = "Bodies"


class Office(LabelBase):
    """
    An office represents a post, seat or position occuppied by an individual
    as a result of an election.

    For example: Senator, Governor, President, Representative

    In the case of executive positions, like governor or president, the office
    is tied directlty to a jurisdiction. Otherwise, the office ties to a body
    tied to a jurisdiction.
    """
    division = models.ForeignKey(Division)
    jurisdiction = models.ForeignKey(Jurisdiction, null=True)
    body = models.ForeignKey(Body, null=True)
