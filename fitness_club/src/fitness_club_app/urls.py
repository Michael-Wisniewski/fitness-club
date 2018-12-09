from django.conf.urls import include, url
from django.contrib import admin
from landing_page.views import LandingPageView

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',
                            namespace='blog',
                            app_name='blog'))
]
