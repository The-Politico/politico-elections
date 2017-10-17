import uuid

from django.db import models
from uuslug import uuslug


class UUIDBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class LinkBase(UUIDBase):
    note = models.CharField(
        max_length=300,
        blank=True,
        help_text="A short, optional note related to an object."
    )
    url = models.URLField(help_text="A hyperlink related to an object.")

    class Meta:
        abstract = True


class SlugBase(UUIDBase):
    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    class Meta:
        abstract = True


class NameBase(SlugBase):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = uuslug(
            self.name,
            instance=self,
            max_length=255,
            separator='-',
            start_no=2
        )
        super(NameBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self): # noqa
        return self.name


class LabelBase(NameBase):
    label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self): # noqa
        return self.label


class SelfRelatedBase(models.Model):
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    class Meta:
        abstract = True


class EffectiveDateBase(models.Model):
    effective = models.BooleanField(default=True)
    effective_start = models.DateTimeField(null=True)
    effective_end = models.DateTimeField(null=True)

    class Meta:
        abstract = True
