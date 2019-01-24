from django.conf.urls import url
from . import views

module_name = 'slider_backend'

urlpatterns = [
    url(r'^$',
            views.SlidesListView.as_view(section=module_name),
            name='slides_list'),
    url(r'^slide_create/$',
            views.SlideCreateView.as_view(section=module_name),
            name='slide_create')
]