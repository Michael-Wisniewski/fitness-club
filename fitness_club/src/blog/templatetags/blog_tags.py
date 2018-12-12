from django import template

register = template.Library()

@register.inclusion_tag('blog/blog_content_shortcut.html')
def blog_content_shortcut(count=3):
    posts = {'post1': 'cos tam', 'post2': 'cos tam'}
    return {'posts': posts}