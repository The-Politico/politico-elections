"""
Office result pages are for executive offices only.

URL PATTERNS
FEDERAL: /election-results/{YEAR}/{OFFICE}/
STATE:   /election-results/{YEAR}/{STATE}/{OFFICE}/
"""

from django.shortcuts import get_object_or_404

from election.models import ElectionCycle, ElectionDay, Race
from entity.models import Jurisdiction, Office
from geography.models import Division
from theshow.models import PageContent

from .base import BaseView


class FederalExecutiveRacePage(BaseView):
    model = Race
    context_object_name = 'race'
    template_name = 'theshow/races/race.exec.fed.live.html'

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
    template_name = 'theshow/races/race.exec.fed.export.html'


class StateExecutiveRacePage(BaseView):
    model = Race
    context_object_name = 'race'
    template_name = 'theshow/races/race.exec.state.live.html'

    def get_queryset(self):
        state = Division.objects.get(slug=self.kwargs.get('state'))
        return self.model.objects.filter(office__division=state)

    def get_object(self):
        cycle = ElectionCycle.objects.get(slug=self.kwargs.get('year'))
        state = Division.objects.get(slug=self.kwargs.get('state'))
        print(self.kwargs.get('office'))
        office = Office.objects.get(
            slug=self.kwargs.get('office'),
            division=state
        )
        return get_object_or_404(
            Race,
            office=office,
            cycle=cycle
        )

    def get_context_data(self, **kwargs):
        context = super(StateExecutiveRacePage, self).get_context_data(
            **kwargs
        )
        state = Division.objects.get(slug=self.kwargs.get('state'))
        election_day = ElectionDay.objects.get(date=self.kwargs.get('date'))
        office = Office.objects.get(
            slug=self.kwargs.get('office'),
            division=state
        )
        race = office.races.get(cycle=election_day.cycle)
        election = race.elections.get(election_day=election_day)
        candidates = election.get_candidates_by_party()
        context['election_day'] = election_day
        context['election'] = election
        context['candidates'] = candidates
        context['year'] = self.kwargs.get('year')
        context['office'] = office
        context['state'] = state
        try:
            page_content = PageContent.get_office_content(
                PageContent, office, election_day
            )
            context['chatter'] = page_content.chatter
        except:
            page_content = None
            context['chatter'] = None
        return context


class StateExecutiveRacePageExport(StateExecutiveRacePage):
    template_name = 'theshow/races/race.exec.state.export.html'
