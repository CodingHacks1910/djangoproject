from django import template
from markdownx.utils import markdownify

register = template.Library()

@register.filter(name = 'markdown')
def markdown(text):
    return markdownify(text)