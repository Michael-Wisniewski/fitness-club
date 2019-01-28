from fitness_club_app.extras import Section
from account.extras import EmployeeLoginRequired
from fitness_club_app.extras import AjaxRequired
from django.views.generic import View, TemplateView, View, UpdateView, DeleteView, CreateView
from blog.models import Post
from preserialize.serialize import serialize
from django.http import JsonResponse
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect

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
    template_name = 'blog_backend/post_create_and_edit.html'
    model = Post
    form_class = PostForm
    initial = {'cancel_url': reverse_lazy('blog_backend:posts_list')}
    success_url = reverse_lazy('blog_backend:posts_list')

class PostDeleteView(Section, EmployeeLoginRequired, DeleteView):
    template_name = 'blog_backend/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog_backend:posts_list')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(PostDeleteView, self).post(request, *args, **kwargs)
    
class PostCreateView(Section, EmployeeLoginRequired, CreateView):
    template_name = 'blog_backend/post_create_and_edit.html'
    model = Post
    form_class = PostForm
    initial = {'cancel_url': reverse_lazy('blog_backend:posts_list')}
    success_url = reverse_lazy('blog_backend:posts_list')
    