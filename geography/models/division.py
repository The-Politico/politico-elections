from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import EffectiveDateBase, LabelBase, NameBase, SelfRelatedBase


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

    peers = models.ManyToManyField(
        'self',
        through='PeerRelationship',
        symmetrical=False,
        related_name='+',
        help_text="Peers represent geographic divisions that intersect but "
                  "do not necessarily have a parent/child relationship. The "
                  "relationship between a congressional district and a "
                  "precinct is an example of a peer relationship."
    )

    def add_peer(self, division, intersection=None, symm=True):
        """
        Adds paired relationships between peer divisions.

        Optional intersection represents the portion of the area of the related
        division intersecting this division. You can only specify an
        intersection on one side of the relationship when adding a peer.
        """
        relationship, created = PeerRelationship.objects.update_or_create(
            from_division=self,
            to_division=division,
            defaults={'intersection': intersection}
        )
        if symm:
            division.add_peer(self, None, False)
        return relationship

    def remove_peer(self, division, symm=True):
        PeerRelationship.objects.filter(
            from_division=self,
            to_division=division
        ).delete()
        if symm:
            division.remove_peer(self, False)

    def set_intersection(self, division, intersection):
        PeerRelationship.objects.filter(
            from_division=self,
            to_division=division
        ).update(intersection=intersection)

    def get_intersection(self, division):
        try:
            return PeerRelationship.objects.get(
                from_division=self,
                to_division=division
            ).intersection
        except ObjectDoesNotExist:
            raise Exception('No peer relationship with that division.')


class PeerRelationship(models.Model):
    """
    Each PeerRelationship instance represents one side of a paired relationship
    between peer divisions.
    """
    from_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name="+"
    )
    to_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name="+"
    )
    intersection = models.DecimalField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(1.0)
        ],
        max_digits=7,
        decimal_places=6,
        null=True, blank=True,
        help_text="The portion of the to_division that intersects this "
                  "division."
    )

    class Meta:
        # Don't allow duplicate relationships between divisions
        unique_together = ('from_division', 'to_division')
