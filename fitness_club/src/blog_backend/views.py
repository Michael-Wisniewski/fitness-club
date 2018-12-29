from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from fitness_club_app.extras import AjaxRequired
from django.views.generic import View, TemplateView, View, UpdateView
from blog.models import Post
from preserialize.serialize import serialize
from django.http import JsonResponse

class PostsListView(Section, EmployeeLoginRequired, TemplateView):
    template_name = 'blog_backend/posts_list.html'

class PostsListData(EmployeeLoginRequired, AjaxRequired, View):

    def get_posts_serialize_template(self):

        author_template = {
            'fields': [ 'first_name', 'last_name']
        }

        posts_template = { 
            'fields': ['id', 'title', 'author', 'publish', 'status'],
            'related': { 'author':  author_template } 
        }

        return posts_template

    def get(self, request):
        posts = Post.objects.all().order_by('-publish')
        posts_serialized = serialize(posts, **self.get_posts_serialize_template())
        return JsonResponse({'data': posts_serialized}, safe=False)

class PostEditView(Section, EmployeeLoginRequired, UpdateView):
    template_name = 'blog_backend/post_edit.html'
    model = Post
    fields = ['title', ]
