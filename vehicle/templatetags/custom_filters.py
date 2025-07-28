# In your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def absolute(value):
    """Returns the absolute value of a number"""
    try:
        return abs(value)
    except (TypeError, ValueError):
        return value