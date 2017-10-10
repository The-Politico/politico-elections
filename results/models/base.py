from django.db import models
from uuslug import uuslug

class SlugModel(models.Model):
    label = models.CharField(max_length=255)
    short_label = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(
        blank=True, max_length=255, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(
            self.label,
            instance=self,
            max_length=255,
            separator='-',
            start_no=2
        )
        super(SlugModel, self).save(*args, **kwargs)

    def __str__(self): # noqa
        return self.label

    class Meta:
        abstract = True
