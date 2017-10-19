"""
Body result pages.

URL PATTERNS
FEDERAL: /election-results/{YEAR}/{BODY}/
STATE:   /election-results/{YEAR}/{STATE}/{BODY}/
"""
from django.shortcuts import get_object_or_404

from entity.models import Body, Jurisdiction
from geography.models import Division, DivisionLevel

from .base import BaseView


class FederalBodyPage(BaseView):
    model = Body
    context_object_name = 'body'
    template_name = 'showtime/bodies/body.fed.live.html'

    def get_queryset(self):
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        return self.model.objects.filter(jurisdiction=fed)

    def get_object(self):
        fed = Jurisdiction.objects.get(name='U.S. Federal Government')
        return get_object_or_404(
            Body,
            slug=self.kwargs.get('body'),
            jurisdiction=fed,
        )

    def get_context_data(self, **kwargs):
        context = super(FederalBodyPage, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        return context


class FederalBodyPageExport(FederalBodyPage):
    template_name = 'showtime/bodies/body.fed.export.html'


class StateBodyPage(BaseView):
    model = Body
    context_object_name = 'body'
    template_name = 'showtime/bodies/body.state.live.html'

    def get_queryset(self):
        states = DivisionLevel.objects.get(name='state')
        return self.model.objects.filter(jurisdiction__division__level=states)

    def get_object(self):
        state = Division.objects.get(slug=self.kwargs.get('state'))
        print(state, self.kwargs.get('body'))
        return get_object_or_404(
            Body,
            slug=self.kwargs.get('body'),
            jurisdiction__division=state
        )

    def get_context_data(self, **kwargs):
        context = super(StateBodyPage, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['state'] = self.kwargs.get('state')
        return context


class StateBodyPageExport(StateBodyPage):
    template_name = 'showtime/bodies/body.state.export.html'
