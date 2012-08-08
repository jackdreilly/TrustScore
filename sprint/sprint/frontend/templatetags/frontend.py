from django import template
register = template.Library()

## tags.py
@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''