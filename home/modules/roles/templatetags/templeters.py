from django import template

register = template.Library()

@register.filter
def return_username(value):
    try:
        user = value['user']
    except AttributeError:
        print("ModelChoiceField object has no attribute username")
    return user.username

register.filter('return_username', return_username)