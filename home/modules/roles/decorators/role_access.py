from ..models import Role
from django.shortcuts import render

def access(argument='A'):
    """
    Decorator returns forbidden page if user have no access
        for dev site version logic : G <-I <-A => Admin is Inhabitant and Inhabitant is Guest,
        so Admin is also Guest. That means that:
            > Guest rights is for all room-users;
            > Inhabitant for Inhabitant and Admin;
            > Admin is only for Admin;
        So we use `user_access_level > access_level` to find if user access is more than needed so we
        can forbid it.
    """
    def access_wrapper(function):
        def wrapper(*args, **kwargs):
            user = args[0].user
            role = Role.objects.get(user=user)
            table = get_access_table()
            access_level = table[argument[0].upper()]
            user_access_level = table[role.role]

            if user_access_level > access_level:
                return render(args[0], 'forbidden.html', {'user': user})

            return function(*args, **kwargs)
        return wrapper
    return access_wrapper


def get_access_table():
    table = dict()
    i = 1
    for role in Role.roles:
        table[role[0]] = i
        i += 1
    return table