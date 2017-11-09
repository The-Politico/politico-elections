from django.db import models

from geography.models import Division


class CensusTable(models.Model):
    """
    A census series.
    """
    SERIES_CHOICES = (
        ('acs1', 'American Community Survey 1-year data profiles'),
        ('acs5', 'American Community Survey 5-year'),
        ('sf1', 'Decennial census, SF1'),
        ('sf3', 'Decennial census, SF3'),
    )
    series = models.CharField(max_length=4, choices=SERIES_CHOICES)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.title:
            return '{} {} ({})'.format(self.year, self.code, self.title)
        return '{} {}'.format(self.year, self.code)


class CensusLabel(models.Model):
    """
    Custom labels for census variables that allow us to
    aggregate variables.
    """
    AGGREGATION_CHOICES = (
        ('s', 'Sum'),
        ('a', 'Average'),
        ('m', 'Median'),
    )
    label = models.CharField(max_length=100)
    aggregation = models.CharField(
        max_length=1,
        choices=AGGREGATION_CHOICES,
        default='s'
    )
    table = models.ForeignKey(
        CensusTable,
        on_delete=models.CASCADE,
        related_name='labels'
    )

    def __str__(self):
        return self.label


class CensusVariable(models.Model):
    """
    Individual variables on census series to pull, e.g.,  "001E" on ACS table
    19001, the total for household income.
    """
    code = models.CharField(
        max_length=4,
        help_text="3 digit code for variable and 'E', e.g., 001E."
    )
    table = models.ForeignKey(
        CensusTable,
        related_name='variables',
        on_delete=models.CASCADE
    )
    label = models.ForeignKey(
        CensusLabel,
        related_name='variables',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return '{}_{}'.format(
            self.table.code,
            self.code
        )


class CensusEstimate(models.Model):
    """
    Individual census series estimates.
    """
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='census_estimates'
    )
    variable = models.ForeignKey(
        CensusVariable,
        on_delete=models.CASCADE,
        related_name='estimates'
    )
    estimate = models.FloatField()

    @property
    def full_code(self):
        return '{}_{}'.format(
            self.variable.table.code,
            self.variable.code
        )

    def __str__(self):
        return '{} {}_{}'.format(
            self.division.code,
            self.variable.table.code,
            self.variable.code
        )
