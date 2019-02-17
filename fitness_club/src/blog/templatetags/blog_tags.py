from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    post_quantity = Post.published.count()
    if post_quantity != 1:
        response = 'There are <span>{}</span> posts published.'.format(post_quantity)
    else:
        response = 'There is <span>1</span> post published.'
    return response

@register.inclusion_tag('blog/tags_templates/posts_list.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'posts_list': latest_posts}

@register.inclusion_tag('blog/tags_templates/posts_list.html')
def show_most_commented_posts(count=5):
    most_commented_posts =  Post.published.annotate(total_comments=Count('comments'))\
                                          .order_by('-total_comments')[:count]
    return {'posts_list': most_commented_posts}                                

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.inclusion_tag('blog/tags_templates/blog_content_shortcut.html')
def blog_content_shortcut():
    archive_posts = []
    posts_query = Post.published.all()[:13]
    posts = posts_query[:3]
    archive_posts = posts_query[3:13]

    return {'posts': posts, 'archive_posts': archive_posts}