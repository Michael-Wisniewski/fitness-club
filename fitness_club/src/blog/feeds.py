from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from bs4 import BeautifulSoup
import markdown

class LatestPostsFeed(Feed):
    title = 'Fitness Club Blog'
    link = '/blog/'
    description = 'New blog posts'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        html_text = markdown.markdown(item.body)
        plain_text = BeautifulSoup(html_text).get_text()
        if len(plain_text) > 100:
            plain_text = plain_text[0:97] + '...'
        return plain_text
    