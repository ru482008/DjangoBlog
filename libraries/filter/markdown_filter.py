from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    html = md.markdown(value, extensions=["markdown.extensions.fenced_code"])
    return html
