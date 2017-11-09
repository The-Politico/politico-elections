from django.contrib import admin

from election.models import (Candidate, CandidateElection, Election,
                             ElectionCycle, ElectionDay, ElectionType, Party,
                             Race)

admin.site.register(Race)
admin.site.register(Party)
admin.site.register(Election)
admin.site.register(CandidateElection)
admin.site.register(ElectionDay)
admin.site.register(ElectionType)
admin.site.register(ElectionCycle)
admin.site.register(Candidate)
