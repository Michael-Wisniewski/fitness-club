from fitness_club_app.extras import Section
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm
from taggit.models import Tag
from django.db.models import Count
from haystack.query import SearchQuerySet

class SearchPosts():
    def get(self, request, *args, **kwargs):
        response = super(SearchPosts, self).get(self, request, *args, **kwargs)
        query = request.GET.get('query', False)
        if query is not False:
            return HttpResponseRedirect(reverse('blog:posts_search')\
                  +'?query={}'.format(query))
        else:
            return response

class PostListView(Section, SearchPosts, ListView):
    template_name = 'blog/posts/posts_list.html'
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    tag = ''

    def get_queryset(self, **kwargs):
        posts = super(PostListView, self).get_queryset(**kwargs)
        if 'tag_slug' in self.kwargs:
            self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            posts = posts.filter(tags__in=[self.tag])
        return posts

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class PostDetailView(Section, SearchPosts, FormMixin, DetailView):
    template_name = 'blog/posts/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_queryset(self, **kwargs): 
        qs = Post.published.filter(publish__year=self.kwargs['year'],
                                   publish__month=self.kwargs['month'],
                                   publish__day=self.kwargs['day'])
        if not qs:
            raise Http404()
        else:
            return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = context['object'].comments.filter(active=True)
        context['form'] = self.get_form()
        context['new_comment'] = self.request.GET.get('new_comment', False)
        post_tags_ids = self.object.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                            .exclude(id=self.object.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                            .order_by('-same_tags', '-publish')[:4]
        context['similar_posts'] = similar_posts                                      
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, self.object)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, post):
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        return HttpResponseRedirect(post.get_absolute_url()+'?new_comment=true')

class PostShareView(Section, SearchPosts, FormView):
    template_name = 'blog/posts/post_share.html'
    form_class = EmailPostForm
    success_url = 'sended/'

    def get_initial(self, **kwargs):
        initial = super(PostShareView, self).get_initial(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'], status='published')
        initial['title'] = post.title
        initial['url'] = self.request.build_absolute_uri(post.get_absolute_url())
        return initial

    def form_valid(self, form):
        form.send_email()
        return super(PostShareView, self).form_valid(form)

class PostShareSendedView(Section, SearchPosts, DetailView):
    model = Post
    template_name = 'blog/posts/post_share_sended.html'

class PostSearchView(Section, ListView):
    template_name = 'blog/posts/post_search.html'
    context_object_name = 'posts'
    paginate_by = 5
    results_quantity = 0
    form = SearchForm()

    def get_queryset(self):
        posts = []

        if 'query' in self.request.GET:
            form = SearchForm(self.request.GET)
        
            if form.is_valid():
                cd = form.cleaned_data
                sqs_total = SearchQuerySet().models(Post)\
                            .filter(content=cd['query']).load_all()
                query_str = cd['query']
                bold_query_str = '<span style="color:#f11cd8">'\
                                    +query_str\
                                  +'</span>'

                for sqs in sqs_total:
                    post = sqs.object
                    post.title = post.title.replace(query_str, bold_query_str)
                    post.body = post.body.replace(query_str, bold_query_str)
                    posts.append(post)
        
        self.results_quantity = len(posts)                    

        return posts

    def get_context_data(self, *args, **kwargs):
        context = super(PostSearchView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['query'] = self.request.GET.get('query', None)
        context['hide_search_bar'] = True
        context['results_quantity'] = self.results_quantity
        return context