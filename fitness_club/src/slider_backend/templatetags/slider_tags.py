from django import template
from ..models import SliderPicture

register = template.Library()

@register.inclusion_tag('slider_backend/tags_templates/slider.html')
def slider_shortcut():
    slides = SliderPicture.objects.all()
    return {'slides': slides}