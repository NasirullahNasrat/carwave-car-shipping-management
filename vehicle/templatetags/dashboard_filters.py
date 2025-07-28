from django import template

register = template.Library()

@register.filter
def absolute(value):
    """Return the absolute value"""
    try:
        return abs(float(value))
    except (ValueError, TypeError):
        return value