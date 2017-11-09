"""
Election cycle results page.

URL PATTERNS:
/election-results/{YEAR}/
"""

from django.shortcuts import get_object_or_404

from election.models import ElectionCycle

from .base import BaseView


class CyclePage(BaseView):
    """
    **Preview URL**: :code:`/election-results/cycle/{YEAR}/`
    """
    model = ElectionCycle
    context_object_name = 'cycle'
    template_name = 'theshow/cycles/cycle.live.html'

    def get_object(self):
        return get_object_or_404(ElectionCycle, slug=self.kwargs.get('year'))

    def get_context_data(self, **kwargs):
        context = super(CyclePage, self).get_context_data(**kwargs)
        # more context TK...
        return context


class CyclePageExport(CyclePage):
    """
    **Publish URL**: :code:`/election-results/{YEAR}/`
    """
    template_name = 'theshow/cycles/cycle.export.html'
