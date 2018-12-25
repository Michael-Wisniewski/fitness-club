from django.conf.urls import url
from . import views

module_name = 'blog_backend'

urlpatterns = [
    url(r'^$',
            views.PostListView.as_view(section=module_name),
            name='posts_list_backend'),
]