from django.db import models

from core.models import NameBase, SlugBase, UUIDBase


<<<<<<< Updated upstream
class Person(LabelBase):
=======
class Person(SlugBase, NameBase, UUIDBase):
    """
    uuid
    slug
    name
    """
>>>>>>> Stashed changes
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        # person-sluggedname

        full_name = '{0}{1}{2}'.format(
            self.first_name,
            '{0}'.format(
                ' ' + self.middle_name + ' ' if self.middle_name else ' '
            ),
            self.last_name
        )

        self.name = full_name
        super(Person, self).save(*args, **kwargs)
