from fitness_club_app.extras import Section
from django.views.generic import ListView, DetailView, FormView
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import EmailPostForm

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

class PostShareView(Section, FormView):
    template_name = 'blog/posts/post_share.html'
    form_class = EmailPostForm
    success_url = 'sended/'

    def get_initial(self, **kwargs):
        initial = super(PostShareView, self).get_initial( **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'], status='published')
        initial['title'] = post.title
        initial['url'] = self.request.build_absolute_uri(post.get_absolute_url())
        return initial

    def form_valid(self, form):
        form.send_email()
        return super(PostShareView, self).form_valid(form)

class PostShareSendedView(Section, DetailView):
    model = Post
    template_name = 'blog/posts/post_share_sended.html'