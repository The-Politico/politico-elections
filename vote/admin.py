from django.contrib import admin

from .models import APElectionMeta, Votes


class VotesAdmin(admin.ModelAdmin):
    list_display = (
        'candidate',
        'election',
        'division',
        'level',
        'count',
        'pct',
    )

    list_editable = ('count', 'pct')

    list_filter = ('division__level', 'candidate_election__election')

    def candidate(self, obj):
        return obj.candidate_election.candidate

    def election(self, obj):
        return obj.candidate_election.election

    def division(self, obj):
        return obj.division

    def level(self, obj):
        return obj.division.level

    candidate.admin_order_field = 'candidate_election__candidate__person__last_name'
    election.admin_order_field = 'candidate_election__election'
    division.admin_order_field = 'candidate_election__division'


admin.site.register(APElectionMeta)
admin.site.register(Votes, VotesAdmin)
