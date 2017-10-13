from django.contrib import admin
from results.models import Geography, GeographyLevel


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('label', 'state_fips', 'code')
    list_filter = ('geography_level',)
    search_fields = ('code',)


admin.site.register(Geography, GeographyAdmin)
admin.site.register(GeographyLevel)
