from django.conf.urls import url
from . import views

module_name = 'blog_backend'

urlpatterns = [
    url(r'^posts_list/$',
            views.PostsListView.as_view(section=module_name),
            name='posts_list'),
    url(r'^posts_list_data/$', 
            views.PostsListData.as_view(),
            name='posts_list_data'),
    url(r'^post_edit/$',
            views.PostEditView.as_view(),
            name='post_edit_blind'),
    url(r'^post_edit/(?P<pk>\d+)/$',
            views.PostEditView.as_view(section=module_name),
            name='post_edit'),
    url(r'^post_delete/$',
            views.PostDeleteView.as_view(section=module_name),
            name='post_delete_blind'),
    url(r'^post_delete/(?P<pk>\d+)/$',
            views.PostDeleteView.as_view(section=module_name),
            name='post_delete_blind'),
    url(r'^post_create/$',
            views.PostCreateView.as_view(section=module_name),
            name='post_create')
]