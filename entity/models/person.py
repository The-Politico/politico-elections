from django.db import models

from core.models import LabelBase


class Person(LabelBase):
    """
    uuid
    slug
    name
    label
    short_label
    """
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        name_label = '{0}{1}{2}'.format(
            self.first_name,
            '{0}'.format(
                ' ' + self.middle_name + ' ' if self.middle_name else ' '
            ),
            self.last_name
        )

        self.label = name_label
        self.name = name_label
        self.short_label = self.last_name
        super(Person, self).save(*args, **kwargs)
