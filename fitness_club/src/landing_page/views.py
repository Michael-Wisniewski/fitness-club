from django.views.generic.base import TemplateView

class LandingPageView(TemplateView):
    template_name = "landing_page/home.html"
