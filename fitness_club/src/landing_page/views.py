from django.views.generic.base import TemplateView

class LandingPageView(TemplateView):
    template_name = "landing_page/home.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data( **kwargs)
        context['section'] = 'home'
        return context