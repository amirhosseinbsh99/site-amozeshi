from django import template
register = template.Library()



def my_truncate(paraphs):

    return f'{str(paraphs[:15])} ...'


register.filter('giyo', my_truncate)