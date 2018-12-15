from fitness_club_app.extras import Section
from django.views.generic.base import TemplateView

class LandingPageView(Section, TemplateView):
    template_name = "landing_page/home.html"