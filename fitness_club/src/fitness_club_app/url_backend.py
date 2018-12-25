from django.conf.urls import include, url
from landing_page_backend.views import LandingPageView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(section='landing_page_backend'), 
            name='landing_page_backend'),
    
]