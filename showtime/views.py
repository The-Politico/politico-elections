from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from entity.models import Body
from geography.models import Division, DivisionLevel


class StatePage(DetailView):
    model = Division
    context_object_name = 'state'
    queryset = Division.objects.all()
    template_name = 'showtime/state/state.live.html'

    def get_object(self):
        return get_object_or_404(Division, slug=self.args[1])


class StatePageExport(StatePage):
    template_name = 'showtime/state/state.export.html'


class FederalBodyPage(DetailView):
    model = Body
    context_object_name = 'body'
    queryset = Body.objects.all()
    template_name = 'showtime/body/body.live.html'

    def get_object(self):
        return get_object_or_404(Body, slug=self.args[1])


class FederalBodyPageExport(FederalBodyPage):
    template_name = 'showtime/body/body.export.html'
