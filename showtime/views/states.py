"""
State result pages.

URL PATTERNS
/election-results/{YEAR}/{STATE}/
"""
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from geography.models import Division, DivisionLevel


class StatePage(DetailView):
    model = Division
    context_object_name = 'state'
    template_name = 'showtime/states/state.live.html'

    def get_queryset(self):
        level = DivisionLevel.objects.get(name='state')
        return self.model.objects.filter(level=level)

    def get_object(self):
        return get_object_or_404(Division, slug=self.kwargs.get('state'))

    def get_context_data(self, **kwargs):
        context = super(StatePage, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        return context


class StatePageExport(StatePage):
    template_name = 'showtime/states/state.export.html'
