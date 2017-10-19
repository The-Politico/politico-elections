"""
Base context for all pages, e.g., data needed to render navigation.
"""

from django.views.generic import DetailView


class BaseView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        # Context TK
        return context
