from django.conf.urls import include, url
from landing_page_backend.views import LandingPageView
from account.views import EmployeeLoginView, EmployeeLogut

urlpatterns = [
    url(r'^$', LandingPageView.as_view(section='landing_page_backend'),
            name='landing_page_backend'),
    url(r'^login/$', EmployeeLoginView.as_view(),
            name='login_backend'),
    url(r'^logout/$', EmployeeLogut,
            name='logout_backend'),
    url(r'^blog_backend/', include('blog_backend.urls',
            namespace='blog_backend',
            app_name='blog_backend')),
]