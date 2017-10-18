from django.contrib import admin

from election.models import (Election, ElectionCycle, ElectionDay,
                             ElectionType, Race)

admin.site.register(Race)
admin.site.register(Election)
admin.site.register(ElectionDay)
admin.site.register(ElectionType)
admin.site.register(ElectionCycle)
