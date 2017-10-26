from django.db import models
from uuslug import uuslug

from core.models import NameBase, SlugBase, UIDBase


class Person(UIDBase, SlugBase, NameBase):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        uid: person-{slug}
        """

        full_name = '{0}{1}{2}'.format(
            self.first_name,
            '{0}{1}'.format(
                ' ' + self.middle_name + ' ' if self.middle_name else ' ',
                ' ' + self.suffix if self.suffix else '',
            ),
            self.last_name
        )

        self.name = full_name
        self.slug = uuslug(
            self.name,
            instance=self,
            max_length=100,
            separator='-',
            start_no=2
        )
        self.uid = 'person-{}'.format(self.slug)

        super(Person, self).save(*args, **kwargs)
