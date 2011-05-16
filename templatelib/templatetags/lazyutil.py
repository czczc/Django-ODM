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

@register.filter
def add_hours(date, hours):
    from datetime import timedelta
    return date + timedelta(seconds=hours*3600)
        
@register.filter
def extract_notes(comment):
    import re
    notes = ''
    reg1 = re.compile(r"DataCategory</td><td class='value'>(.+?)</td>")
    try:
        notes += reg1.search(comment).group(1) + ', '
    except:
        pass
    reg2 = re.compile(r"Description</td><td class='value'>(.+?)</td>")
    try:
        notes += reg2.search(comment).group(1) + ', '
    except:
        pass
    reg3 = re.compile(r"Comments</td><td class='value'>(.+?)</td>")
    try:
        notes += reg3.search(comment).group(1)
    except:
        pass
    if not notes:
        from django.utils.html import strip_tags
        notes = strip_tags(comment)

    return notes
    