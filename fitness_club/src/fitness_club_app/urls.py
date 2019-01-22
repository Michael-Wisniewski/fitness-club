from django.conf.urls import include, url
from landing_page.views import LandingPageView
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^$', LandingPageView.as_view(section='home'), 
            name='landing_page'),
    url(r'^blog/', include('blog.urls',
            namespace='blog',
            app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib,sitemaps.views.sitemap'),
]
