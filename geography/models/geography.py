import json

from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from core.models import EffectiveDateBase
from .division import Division, DivisionLevel


class Geography(EffectiveDateBase):
    D3 = '''
        <div id="map{0}"></div>
        <script>
        var data{0} = {1};
        var feature{0} = topojson.feature(
            data{0}, data{0}.objects['-']);
        var svg{0} = d3.select("#map{0}").append("svg")
            .attr("width", {2})
            .attr("height", {2});
        svg{0}.append("path").datum(feature{0})
            .attr("d", d3.geoPath().projection(
                d3.geoAlbersUsa().scale(1)
                .fitSize([{2}, {2}], feature{0})
            ));
        </script>
    '''

    def small_preview(self):
        return mark_safe(self.D3.format(self.pk, self.topojson, '60'))

    def large_preview(self):
        return mark_safe(self.D3.format(self.pk, self.topojson, '400'))

    def file_size(self):
        return '~{} kB'.format(
            round(len(json.dumps(self.topojson)) / 1000)
        )

    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name="geographies"
    )
    subdivision_level = models.ForeignKey(
        DivisionLevel,
        on_delete=models.PROTECT,
        related_name="+"
    )
    simplification = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(1.0)
        ],
        help_text="Minimum quantile of planar \
        triangle areas for simplfying topojson."
    )
    topojson = JSONField()

    def __str__(self):
        return '{} - {} map, {}'.format(
            self.division.label,
            self.division.level.name,
            self.simplification
        )

    class Meta:
        verbose_name_plural = "Geographies"
