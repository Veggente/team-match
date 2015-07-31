from django import template
register = template.Library()

@register.inclusion_tag('groupem/header.html')
def render_header():
    return
