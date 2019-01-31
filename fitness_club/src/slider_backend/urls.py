from django.conf.urls import url
from . import views

module_name = 'slider_backend'

urlpatterns = [
    url(r'^$',
            views.SlidesListView.as_view(section=module_name),
            name='slides_list'),
    url(r'^slide_create/$',
            views.SlideCreateView.as_view(section=module_name),
            name='slide_create'),
    url(r'^slides_order/$',
            views.UpdateSlidesOrder.as_view(),
            name='slides_order'),
    url(r'^slide_delete/(?P<pk>\d+)/$',
            views.SlideDeleteView.as_view(section=module_name),
            name='slide_delete')
]