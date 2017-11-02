from django.contrib import admin

from theshow.models import PersonImage

from .models import Body, Jurisdiction, Office, Person


class PersonImageInline(admin.StackedInline):
    model = PersonImage
    extra = 0
    fields = (
        'tag',
        'image',
        'preview',
    )
    readonly_fields = ('preview',)


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PersonImageInline,
    ]
    search_fields = ('name',)


admin.site.register(Body)
admin.site.register(Jurisdiction)
admin.site.register(Office)
admin.site.register(Person, PersonAdmin)
