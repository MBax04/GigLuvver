# custom_filters.py

from django import template

register = template.Library()

@register.filter(name='get_key')
def get_key(dictionary, key):
    if dictionary is not None:
        return dictionary.get(key)
    else:
        return None
