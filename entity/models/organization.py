from django.db import models
from uuslug import slugify, uuslug

from core.constants import MINIMUM_STOPWORDS
from core.models import LabelBase, NameBase, SelfRelatedBase, SlugBase, UIDBase
from geography.models import Division


class Jurisdiction(UIDBase, SlugBase, NameBase, SelfRelatedBase):
    """
    A Jurisdiction represents a logical unit of governance, comprising of
    a collection of legislative bodies, administrative offices or public
    services.

    For example: the United States Federal Government, the Government
    of the District of Columbia, Columbia Missouri City Government, etc.

    uuid
    slug
    name
    label
    short_label
    parent
    """
    division = models.ForeignKey(Division, null=True)

    def save(self, *args, **kwargs):
        """
        uid: {division.uid}_jurisdiction:{slug}
        """
        stripped_name = ' '.join(
            w for w in self.name.split()
            if w not in MINIMUM_STOPWORDS
        )

        self.slug = uuslug(
            stripped_name,
            instance=self,
            max_length=100,
            separator='-',
            start_no=2
        )
        self.uid = '{}_jurisdiction:{}'.format(
            self.division.uid, slugify(stripped_name))

        super(Jurisdiction, self).save(*args, **kwargs)


class Body(UIDBase, LabelBase, SelfRelatedBase):
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

    UUID
    """
    slug = models.SlugField(blank=True, max_length=255, editable=True)

    jurisdiction = models.ForeignKey(Jurisdiction)

    class Meta:
        verbose_name_plural = "Bodies"

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        """
        uid: {jurisdiction.uid}_body:{slug}
        """
        stripped_name = ' '.join(
            w for w in self.name.split()
            if w not in MINIMUM_STOPWORDS
        )

        if not self.slug:
            self.slug = uuslug(
                stripped_name,
                instance=self,
                max_length=100,
                separator='-',
                start_no=2
            )
        self.uid = '{}_body:{}'.format(
            self.jurisdiction.uid, slugify(stripped_name))

        super(Body, self).save(*args, **kwargs)


class Office(UIDBase, LabelBase):
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

    UUID
    """
    slug = models.SlugField(blank=True, max_length=255, editable=True)

    division = models.ForeignKey(Division, related_name='offices')
    jurisdiction = models.ForeignKey(
        Jurisdiction, null=True, blank=True, related_name='offices')
    body = models.ForeignKey(
        Body, null=True, blank=True, related_name='offices')

    def __str__(self):
        return self.label

    def is_executive(self):
        return self.body is None

    def save(self, *args, **kwargs):
        """
        uid: {body.uid | jurisdiction.uid}_office:{slug}
        """
        stripped_name = ' '.join(
            w for w in self.name.split()
            if w not in MINIMUM_STOPWORDS
        )

        if not self.slug:
            self.slug = uuslug(
                stripped_name,
                instance=self,
                max_length=100,
                separator='-',
                start_no=2
            )
        if self.body:
            self.uid = '{}_office:{}'.format(
                self.body.uid, slugify(stripped_name))
        else:
            self.uid = '{}_office:{}'.format(
                self.jurisdiction.uid, slugify(stripped_name))

        super(Office, self).save(*args, **kwargs)
