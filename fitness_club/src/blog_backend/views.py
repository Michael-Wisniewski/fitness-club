from fitness_club_app.extras import Section
from django.views.generic import ListView

class PostListView(Section, ListView):
    template_name = 'blog_backend/posts_list.html'