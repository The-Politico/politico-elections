import os
import uuid

from django.db import models
from django.utils.html import format_html

from core.aws import StorageService
from core.models import AuditTrackBase, UUIDBase
from entity.models import Person


def person_image_path(instance, filename):
    return os.path.join(
        'cdn/images/people',
        instance.person.slug,
        '{}-{}{}'.format(
            instance.tag,
            uuid.uuid4().hex[:6],
            os.path.splitext(filename)[1]
        )
    )


class PersonImage(UUIDBase, AuditTrackBase):
    """
    Image attached to a person, which can be serialized
    by a tag.
    """
    person = models.ForeignKey(Person, related_name='images')
    tag = models.SlugField(
        help_text="Used to serialize images. "
        "<b>Must be unique per person.</b>"
    )
    image = models.ImageField(
        upload_to=person_image_path,
        storage=StorageService()
    )

    def preview(self):
        return format_html(
            '<a href="{0}" target="_blank">'
            '<img src="{0}" style="max-height:100px; max-width: 300px;">'
            '</a>'.format(self.image.url)
        )

    class Meta:
        unique_together = ('person', 'tag')

    def __str__(self):
        return '{} {}'.format(self.person.slug, self.tag)
