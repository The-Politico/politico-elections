"""
Base context for all pages, e.g., data needed to render navigation.
"""

from django.views.generic import DetailView, TemplateView

from core.aws import defaults


class BaseView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['domain'] = defaults.DOMAIN
        context['root_path'] = defaults.ROOT_PATH
        # Context TK
        return context


class LinkPreview(TemplateView):
    template_name = "theshow/preview.html"
