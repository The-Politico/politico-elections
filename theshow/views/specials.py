"""
State result pages.

URL PATTERNS:
/election-results/{YEAR}/{STATE}/special-election/{MMM}-{DD}/

State results special elections on an election day.
"""
from django.shortcuts import get_object_or_404

from election.models import ElectionDay
from geography.models import Division, DivisionLevel
from theshow.models import PageContent

from .base import BaseView

month_codes = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
}


class SpecialElectionPage(BaseView):
    """
    **Preview URL**: :code:`/election-results/special-election/{YEAR}/{STATE}/{MMM}-{DD}/`
    """
    model = Division
    context_object_name = 'state'
    template_name = 'theshow/specials/state.live.html'

    @staticmethod
    def build_context(
        election_datestring,  # Format YYYY-MM-DD
        state_slug,
        context={}
    ):
        """
        Build context through a staticmethod so that we can call it
        without an HTTPRequest when baking to AWS.

        cf. utils.bake.election.special_election
        """
        state = Division.objects.get(slug=state_slug)
        election_day = ElectionDay.objects.get(date=election_datestring)
        cycle = election_day.cycle
        context['year'] = cycle.name
        context['election_day'] = election_day
        context['content'] = PageContent.objects.division_content(
            election_day, state
        )
        context['state'] = state
        return context

    def get_queryset(self):
        level = DivisionLevel.objects.get(name='state')
        return self.model.objects.filter(level=level)

    def get_object(self):
        return get_object_or_404(Division, slug=self.kwargs.get('state'))

    def get_context_data(self, **kwargs):
        context = super(SpecialElectionPage, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['election_day'] = get_object_or_404(
            ElectionDay,
            date__year=self.kwargs.get('year'),
            date__month=month_codes.get(self.kwargs.get('month')),
            date__day=self.kwargs.get('day')
        )
        return context


class SpecialElectionPageExport(SpecialElectionPage):
    """
    **Publish URL**: :code:`/election-results/special-election/{YEAR}/{STATE}/{MMM}-{DD}/`
    """
    template_name = 'theshow/specials/state.export.html'
