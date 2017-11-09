import uuid

from django.db import models


class UUIDBase(models.Model):
    """
    A unique id, self-constructed from a UUID.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class UIDBase(models.Model):
    """
    A unique id conforming to our record identifier conventions.
    """
    uid = models.CharField(
        max_length=500,
        primary_key=True,
        editable=False,
        blank=True
    )

    class Meta:
        abstract = True


class SlugBase(models.Model):
    """Adds a unique slug."""
    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    class Meta:
        abstract = True


class PrimaryKeySlugBase(models.Model):
    """Adds a primary key slug."""
    slug = models.SlugField(
        blank=True,
        max_length=255,
        unique=True,
        editable=False,
        primary_key=True
    )

    class Meta:
        abstract = True


class NameBase(models.Model):
    """Adds a name field."""
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self): # noqa
        return self.name


class LabelBase(NameBase):
    """Adds a label and short label that can be derived from name. """
    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self): # noqa
        return self.label

    def save(self, *args, **kwargs):
        if not self.label:
            self.label = self.name

        super(LabelBase, self).save(*args, **kwargs)


class SelfRelatedBase(models.Model):
    """Adds a self-referrencing foreign key."""
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')

    class Meta:
        abstract = True


class EffectiveDateBase(models.Model):
    """Adds effective date fields."""
    effective = models.BooleanField(default=True)
    effective_start = models.DateTimeField(null=True, blank=True)
    effective_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class AuditTrackBase(models.Model):
    """Adds auto-generated created and updated fields."""
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
