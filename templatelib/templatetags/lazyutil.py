from django import template

register = template.Library()

@register.filter
def to_bool(value):
    if value == None:
        return None
    else:
        return bool(value)
