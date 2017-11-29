"""
State result pages.

URL PATTERNS:
/election-results/{YEAR}/{STATE}/special-election/{MMM}-{DD}/

State results special elections on an election day.
"""
from django.shortcuts import get_object_or_404

from election.models import ElectionDay
from geography.models import Division, DivisionLevel

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

    def get_queryset(self):
        level = DivisionLevel.objects.get(name='state')
        return self.model.objects.filter(level=level)

    def get_object(self):
        return get_object_or_404(Division, slug=self.kwargs.get('state'))

    def get_context_data(self, **kwargs):
        context = super(SpecialElectionPage, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['election_date'] = get_object_or_404(
            ElectionDay,
            date__year=self.kwargs.get('year'),
            date__month=month_codes.get(self.kwargs.get('month')),
            date__day=self.kwargs.get('day')
        )
        context['race'] = None
        return context


class SpecialElectionPageExport(SpecialElectionPage):
    """
    **Publish URL**: :code:`/election-results/special-election/{YEAR}/{STATE}/{MMM}-{DD}/`
    """
    template_name = 'theshow/specials/state.export.html'
