from django.contrib.postgres.fields import JSONField
from django.db import models
from .base import SlugModel


class GeographyLevel(SlugModel):
    NATIONAL = 0
    STATE = 1
    DISTRICT = 2
    COUNTY = 3
    PRECINCT = 4

    CODE_CHOICES = (
        (NATIONAL, 'National'),
        (STATE, 'State'),
        (DISTRICT, 'District'),
        (COUNTY, 'County'),
        (PRECINCT, 'Precinct')
    )

    code = models.PositiveSmallIntegerField(choices=CODE_CHOICES)


class Geography(SlugModel):
    code = models.CharField(max_length=30)
    geojson = JSONField(blank=True, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    state_fips = models.CharField(max_length=2)
    geography_level = models.ForeignKey(GeographyLevel)
    parent = models.ManyToManyField('self', related_name="children")
