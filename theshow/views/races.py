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

    @staticmethod
    def build_context(
        election_datestring,  # Format YYYY-MM-DD
        state_slug,
        office_slug,
        context={}
    ):
        """
        We build context through a staticmethod so that we can call it
        separately from a HttpRequest when baking to AWS.
        """
        state = Division.objects.get(slug=state_slug)
        election_day = ElectionDay.objects.get(date=election_datestring)
        cycle = election_day.cycle
        office = Office.objects.get(
            slug=office_slug,
            division=state
        )
        race = office.races.get(cycle=cycle)
        election = race.elections.get(election_day=election_day)
        candidates = election.get_candidates_by_party()
        context['election_day'] = election_day
        context['election'] = election
        context['candidates'] = candidates
        context['year'] = cycle.name
        context['office'] = office
        context['state'] = state
        context['content'] = PageContent.objects.office_content(
            election_day, office
        )
        # Redundant with get_object
        context['race'] = race
        return context

    def get_queryset(self):
        state = Division.objects.get(slug=self.kwargs.get('state'))
        return self.model.objects.filter(office__division=state)

    def get_object(self):
        cycle = ElectionCycle.objects.get(slug=self.kwargs.get('year'))
        state = Division.objects.get(slug=self.kwargs.get('state'))
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
        return self.build_context(
            election_date=self.kwargs.get('date'),
            state_slug=self.kwargs.get('state'),
            office_slug=self.kwargs.get('office'),
            context=context
        )


class StateExecutiveRacePageExport(StateExecutiveRacePage):
    template_name = 'theshow/races/race.exec.state.export.html'
