from django.conf.urls import url
from . import views

module_name = 'blog'

urlpatterns = [
    url(r'^$', 
            views.PostListView.as_view(section=module_name),
            name='posts_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            views.PostDetailView.as_view(section=module_name),
            name='post_detail'),
    url(r'^(?P<pk>\d+)/share/$',
            views.PostShareView.as_view(section=module_name),
            name='post_share'),
    url(r'^(?P<pk>\d+)/share/sended/$',
            views.PostShareSendedView.as_view(section=module_name),
            name='post_share_sended'),
]