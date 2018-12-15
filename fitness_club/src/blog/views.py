from fitness_club_app.extras import Section
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Post

class PostListView(Section, ListView):
    template_name = 'blog/posts/posts_list.html'
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3

class PostDetailView(Section, DetailView):
    template_name = 'blog/posts/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self, **kwargs): 
        qs = Post.published.filter(publish__year=self.kwargs['year'],
                                   publish__month=self.kwargs['month'],
                                   publish__day=self.kwargs['day'])
        
        if not qs:
            raise Http404()
        else:
            return qs