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
    url(r'^slider_backend/', include('slider_backend.urls',
            namespace='slider_backend',
            app_name='slider_backend')),
    url(r'^employees/', include('employees_backend.urls',
            namespace='employees_backend',
            app_name='employees_backend'))
]