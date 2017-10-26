from django.db import models

from core.models import (LabelBase, NameBase, PrimaryKeySlugBase, 
                     SelfRelatedBase, UUIDBase)
from geography.models import Division
from uuslug import slugify


class Jurisdiction(PrimaryKeySlugBase, NameBase, SelfRelatedBase):
    """
    A Jurisdiction represents a logical unit of governance, comprising of
    a collection of legislative bodies, administrative offices or public
    services.

    For example: the United States Federal Government, the Government
    of the District of Columbia, Columbia Missouri City Government, etc.
<<<<<<< Updated upstream
=======

    uuid
    slug
    name
    parent
>>>>>>> Stashed changes
    """
    division = models.ForeignKey(Division, null=True)

    def save(self, *args, **kwargs):
        #tk remove stop words

        super(Jurisdiction, self).save(*args, **kwargs)

        self.slug = '{0}_{1}'.format(division.slug, self.slug)


class Body(SelfRelatedBase):
    """
    A body represents a collection of offices or individuals organized around a
    common government or public service function.

    For example: the U.S. Senate, Florida House of Representatives, Columbia
    City Council, etc.

    name = 'Senate'
    label = 'U.S. Senate'

    * NOTE: Duplicate slugs are allowed on this model to accomodate states:
    slug = senate
    - florida/senate/
    - michigan/senate/
    """
    slug = models.SlugField(blank=True, max_length=255, editable=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    jurisdiction = models.ForeignKey(Jurisdiction)

    def save(self, *args, **kwargs):
        # tk remove stop words

        self.slug = '{0}_{1}'.format(
            self.jurisdiction.slug,
            slugify(self.name)
        )

        super(Body, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Bodies"

    def __str__(self):
        return self.label


class Office(UIDBase):
    """
    An office represents a post, seat or position occuppied by an individual
    as a result of an election.

    For example: Senator, Governor, President, Representative

    In the case of executive positions, like governor or president, the office
    is tied directlty to a jurisdiction. Otherwise, the office ties to a body
    tied to a jurisdiction.

    * NOTE: Duplicate slugs are allowed on this model to accomodate states:
    slug = seat-2
    - florida/house/seat-2/
    - michigan/house/seat-2/
    """
    slug = models.SlugField(blank=True, max_length=255, editable=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    division = models.ForeignKey(Division, related_name='offices')
    jurisdiction = models.ForeignKey(
        Jurisdiction, null=True, blank=True, related_name='offices')
    body = models.ForeignKey(
        Body, null=True, blank=True, related_name='offices')

    def __str__(self):
        return self.label
