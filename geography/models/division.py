from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuslug import slugify, uuslug

from core.constants import DIVISION_LEVEL_CODES
from core.models import (EffectiveDateBase, LabelBase, NameBase,
                         SelfRelatedBase, SlugBase, UIDBase)


class DivisionLevel(UIDBase, SlugBase, NameBase, SelfRelatedBase):
    """
    Level of government or administration at which a division exists.

    For example, federal, state, district, county, precinct, municipal.
    """

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`{levelcode}`
        """
        self.slug = slugify(self.name)
        self.uid = DIVISION_LEVEL_CODES.get(self.slug, self.slug)
        super(DivisionLevel, self).save(*args, **kwargs)


class Division(
    UIDBase, SlugBase, LabelBase, SelfRelatedBase, EffectiveDateBase
):
    """
    A political or administrative geography.

    For example, a particular state, county, district, precinct or
    municipality.
    """
    level = models.ForeignKey(DivisionLevel, related_name='divisions')

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

    intersecting = models.ManyToManyField(
        'self',
        through='IntersectRelationship',
        symmetrical=False,
        related_name='+',
        help_text="Intersecting divisions intersect this one geographically "
                  "but do not necessarily have a parent/child relationship. "
                  "The relationship between a congressional district and a "
                  "precinct is an example of an intersecting relationship."
    )

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`division:{parentuid}_{levelcode}-{code}`
        """
        slug = '{}:{}'.format(self.level.uid, self.code)
        if self.parent:
            self.uid = '{}_{}'.format(self.parent.uid, slug)
        else:
            self.uid = slug
        self.slug = uuslug(
            self.name,
            instance=self,
            max_length=100,
            separator='-',
            start_no=2
        )
        super(Division, self).save(*args, **kwargs)

    def add_intersecting(self, division, intersection=None, symm=True):
        """
        Adds paired relationships between intersecting divisions.

        Optional intersection represents the portion of the area of the related
        division intersecting this division. You can only specify an
        intersection on one side of the relationship when adding a peer.
        """
        relationship, created = IntersectRelationship.objects.update_or_create(
            from_division=self,
            to_division=division,
            defaults={'intersection': intersection}
        )
        if symm:
            division.add_intersecting(self, None, False)
        return relationship

    def remove_intersecting(self, division, symm=True):
        """Removes paired relationships between intersecting divisions"""
        IntersectRelationship.objects.filter(
            from_division=self,
            to_division=division
        ).delete()
        if symm:
            division.remove_intersecting(self, False)

    def set_intersection(self, division, intersection):
        """Set intersection percentage of intersecting divisions."""
        IntersectRelationship.objects.filter(
            from_division=self,
            to_division=division
        ).update(intersection=intersection)

    def get_intersection(self, division):
        """Get intersection percentage of intersecting divisions."""
        try:
            return IntersectRelationship.objects.get(
                from_division=self,
                to_division=division
            ).intersection
        except ObjectDoesNotExist:
            raise Exception('No intersecting relationship with that division.')


class IntersectRelationship(models.Model):
    """
    Each IntersectRelationship instance represents one side of a paired
    relationship between intersecting divisions.

    The intersection field represents the decimal proportion of the
    to_division that intersects with the from_division. It's useful for
    apportioning counts between the areas, for example, population statistics
    from census data.
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
        max_digits=7,
        decimal_places=6,
        null=True, blank=True,
        help_text="The portion of the to_division that intersects this "
                  "division."
    )

    class Meta:
        # Don't allow duplicate relationships between divisions
        unique_together = ('from_division', 'to_division')

    def clean(self):
        if self.intersection < 0.0 or self.intersection > 1.0:
            raise ValidationError(_(
                'Intersection should be a decimal between 0 and 1.'
            ))
