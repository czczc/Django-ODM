from django import template

register = template.Library()

@register.filter
def to_bool(value):
    if value == None:
        return None
    else:
        return bool(value)


@register.filter
def field_type(field, ftype):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == ftype
    except:
        pass
    return False
