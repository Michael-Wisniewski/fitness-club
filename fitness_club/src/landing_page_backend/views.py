from fitness_club_app.extras import Section
from django.views.generic.base import TemplateView
from account.extras import EmployeeLoginRequired

class LandingPageView(Section, EmployeeLoginRequired,  TemplateView):
    template_name = "landing_page_backend/home.html"