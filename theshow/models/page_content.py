import os

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core import exceptions
from django.db import models
from uuslug import uuslug

from core.constants import DIVISION_LEVELS
from core.models import AuditTrackBase, NameBase, PrimaryKeySlugBase, UUIDBase
from election.models import ElectionDay
from geography.models import Division


class PageContentManager(models.Manager):
    """
    Custom manager adds methods to serialize related content blocks.
    """
    @staticmethod
    def serialize_content_blocks(page_content):
        return {
            block.content_type.slug: block.content for block in
            page_content.blocks.all()
        }

    def office_content(self, election_day, office):
        office_type = ContentType.objects.get_for_model(office)

        content = self.get(
            content_type__pk=office_type.pk,
            object_id=office.pk,
            election_day=election_day
        )
        return self.serialize_content_blocks(content)

    def body_content(self, election_day, body, division=None):
        body_type = ContentType.objects.get_for_model(body)

        kwargs = {
            'content_type__pk': body_type.pk,
            'object_id': body.pk,
            'election_day': election_day,
        }

        if division:
            kwargs['division'] = division

        content = self.get(**kwargs)
        return self.serialize_content_blocks(content)

    def division_content(self, election_day, division):
        division_type = ContentType.objects.get_for_model(division)

        try:
            content = self.get(
                content_type__pk=division_type.pk,
                object_id=division.pk,
                election_day=election_day
            )
        except exceptions.ObjectDoesNotExist:
            return None
        return self.serialize_content_blocks(content)


class PageContent(UUIDBase):
    """
    Attaches to several models representing pages:

    Body, Office, Division
    """
    allowed_types = models.Q(app_label='geography', model='division') | \
        models.Q(app_label='entity', model='office') | \
        models.Q(app_label='entity', model='body')
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to=allowed_types,
        on_delete=models.CASCADE
    )
    object_id = models.CharField(max_length=500)
    content_object = GenericForeignKey('content_type', 'object_id')
    election_day = models.ForeignKey(ElectionDay)
    division = models.ForeignKey(Division, null=True, blank=True)
    objects = PageContentManager()

    class Meta:
        unique_together = (
            'content_type',
            'object_id',
            'election_day',
            'division'
        )

    def __str__(self):
        return self.page_location()

    def page_location(self):
        cycle = self.election_day.cycle.name
        if isinstance(self.content_object, Division):
            if self.content_object.level.name == DIVISION_LEVELS['state']:
                path = self.content_object.slug
            else:
                path = ''
        # Offices and Bodies
        else:
            if self.division.level.name == DIVISION_LEVELS['state']:
                path = os.path.join(
                    self.division.slug, self.content_object.slug)
            else:
                path = self.content_object.slug
        return os.sep + os.path.normpath(
            os.path.join(cycle, path)
        ) + os.sep  # normalized URL


class PageContentType(PrimaryKeySlugBase, NameBase):
    """
    The kind of content contained in a content block.
    Used to serialize content blocks.
    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(
                self.name,
                instance=self,
                max_length=100,
                separator='-',
                start_no=2
            )
        super(PageContentType, self).save(*args, **kwargs)


class PageContentBlock(UUIDBase, AuditTrackBase):
    page = models.ForeignKey(PageContent, related_name='blocks')
    content_type = models.ForeignKey(PageContentType, related_name='+')
    content = models.TextField()

    class Meta:
        unique_together = ('page', 'content_type',)

    def __str__(self):
        return self.content_type.name
