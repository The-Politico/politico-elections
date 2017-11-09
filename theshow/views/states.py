"""
State result pages.

URL PATTERNS:
/election-results/{YEAR}/{STATE}/

State results for federal branch, ie, congress and the presidency.

URL PATTERNS:
/election-results/{BRANCH}/{STATE}/

* Branch is either the Body of congress or the Office of the presidency
"""
from django.shortcuts import get_object_or_404

from entity.models import Body, Jurisdiction, Office
from geography.models import Division, DivisionLevel

from .base import BaseView


class StatePage(BaseView):
    """
    **Preview URL**: :code:`/election-results/state/{YEAR}/{STATE}/`
    """
    model = Division
    context_object_name = 'state'
    template_name = 'theshow/states/state.live.html'

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
    """
    **Publish URL**: :code:`/election-results/{YEAR}/{STATE}/`
    """
    template_name = 'theshow/states/state.export.html'


class StateFedPage(StatePage):
    """
    **Preview URL**: :code:`/election-results/state/{YEAR}/{BRANCH}/{STATE}/`

    (:code:`BRANCH` is either a congressional body or the office of the presidency.)
    """
    template_name = 'theshow/states/state.fed.live.html'

    def get_context_data(self, **kwargs):
        context = super(StateFedPage, self).get_context_data(**kwargs)
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        try:
            # Try for congress
            context['branch'] = Body.objects.get(
                slug=self.kwargs.get('branch'),
                jurisdiction=fed
            )
            context['executive'] = False
        except:
            # Handle for president
            context['branch'] = Office.objects.get(
                slug=self.kwargs.get('branch'),
                jurisdiction=fed
            )
            context['executive'] = True
        return context


class StateFedPageExport(StateFedPage):
    """
    **Publish URL**: :code:`/election-results/{YEAR}/{BRANCH}/{STATE}/`

    (:code:`BRANCH` is either a congressional body or the office of the presidency.)
    """
    template_name = 'theshow/states/state.fed.export.html'
