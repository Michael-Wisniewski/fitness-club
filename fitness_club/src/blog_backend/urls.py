from django.conf.urls import url
from . import views

module_name = 'blog_backend'

urlpatterns = [
    url(r'^posts_list/$',
            views.PostsListView.as_view(section=module_name),
            name='posts_list_backend'),
    url(r'^posts_list_data/$', 
            views.PostsListData.as_view(),
            name='posts_list_data'),
    url(r'^post_edit/$',
            views.PostEditView.as_view(),
            name='post_edit_blind'),
    url(r'^post_edit/(?P<pk>\d)$',
            views.PostEditView.as_view(section=module_name),
            name='post_edit'), 
]