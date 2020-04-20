from django import template

register = template.Library()

@register.filter(name='index_counter')
def counter(page_number):
    return int((page_number-1)*10)