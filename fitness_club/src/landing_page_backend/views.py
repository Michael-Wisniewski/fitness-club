from fitness_club_app.extras import Section
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LandingPageView(Section, LoginRequiredMixin, TemplateView):
    template_name = "landing_page_backend/home.html"