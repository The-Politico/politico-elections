from django.contrib import admin
from results.models import Geography, GeoJson, GeoLevel


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('label', 'geolevel', 'geocode')
    list_filter = ('geolevel',)
    search_fields = ('geocode',)


class GeoJsonAdmin(admin.ModelAdmin):
    list_display = ('geography', 'small_preview', 'geography_level',)
    readonly_fields = ('file_size', 'large_preview',)


admin.site.register(Geography, GeographyAdmin)
admin.site.register(GeoLevel)
admin.site.register(GeoJson, GeoJsonAdmin)
