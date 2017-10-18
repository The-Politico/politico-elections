"""
Office result pages.

URL PATTERNS
FEDERAL: /election-results/{YEAR}/{BODY}/{OFFICE}/
STATE:   /election-results/{YEAR}/{STATE}/{BODY}/{OFFICE}/

EXECUTIVE OFFICES:
FEDERAL: /election-results/{YEAR}/{OFFICE}/
STATE:   /election-results/{YEAR}/{STATE}/{OFFICE}/
"""

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from election.models import ElectionCycle, Race
from entity.models import Jurisdiction, Office


class FederalExecutiveRacePage(DetailView):
    model = Race
    context_object_name = 'race'
    template_name = 'showtime/races/race.exec.fed.live.html'

    def get_queryset(self):
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        return self.model.objects.filter(office__jurisdiction=fed)

    def get_object(self):
        cycle = ElectionCycle.objects.get(slug=self.kwargs.get('year'))
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        office = Office.objects.get(
            slug=self.kwargs.get('office'),
            jurisdiction=fed
        )
        return get_object_or_404(
            Race,
            office=office,
            cycle=cycle
        )

    def get_context_data(self, **kwargs):
        context = super(FederalExecutiveRacePage, self).get_context_data(
            **kwargs
        )
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        office = Office.objects.get(
            slug=self.kwargs.get('office'),
            jurisdiction=fed
        )
        context['year'] = self.kwargs.get('year')
        context['office'] = office
        return context


class FederalExecutiveRacePageExport(FederalExecutiveRacePage):
    template_name = 'showtime/races/race.exec.fed.export.html'
