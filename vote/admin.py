from django.contrib import admin

from .models import APElectionMeta, Votes

admin.site.register(APElectionMeta)
admin.site.register(Votes)
