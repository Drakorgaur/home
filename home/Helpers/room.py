import random
import string
from home.modules.roles.models import Role
from home.models import Room


def get_context(request, active='room'):
    context = dict()
    context['user'] = request.user
    role = Role.objects.get(user=request.user)
    context['role'] = role.role
    room = Room.objects.get(user=request.user)
    context['room'] = room
    context['active'] = active
    return context


def get_code():
    code_list = list(string.ascii_uppercase)
    code_list.extend(list(string.digits))
    code = ''
    for i in range(10):
        index = random.randrange(len(code_list))
        code += code_list[index]
    return code

