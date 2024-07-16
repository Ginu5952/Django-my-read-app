from django import template

# singleton
register = template.Library()

@register.filter
def semi_colon_separator(value):
    return value.replace(', ', '; ')