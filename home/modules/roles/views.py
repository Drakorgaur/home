from django.shortcuts import render
from .models import Role
from .forms import RoleForm, FormUsernameBridge
from home.models import Room
from welcome.models import User
from home.modules.roles.decorators.role_access import access
from welcome.forms import AddUserForm
from home.views import init_user_in_room


def get_add_user_form(post=None):
    if post is not None:
        return AddUserForm(post)
    return AddUserForm()

@access('admin')
def test(request):
    return render(request, 'main.html', {'uesr': request.user})


def get_context(request):
    context = dict()
    context['user'] = request.user
    try:
        roles = Role.objects.filter(room=request.user.room)
        role = Role.objects.get(user=request.user)
        context['role'] = role.role
    except Role.DoesNotExist:
        context['error'] = 'roles does not exists. Contact moderator to sole this'
        context['roles'] = None
        context['role'] = None
        return context
    context['roles'] = roles
    return context


def add_user_to_room(user, room):
    if user.room is not None:
        return 'user already have room'
    user.room = room
    user.save()

    init_user_in_room(user, user.room)


def index(request):
    context = get_context(request)
    if request.method == 'POST':
        form = get_add_user_form(request.POST)
        if form.is_valid():
            user_to_add = User.objects.get(username=request.POST['username'])
            context['form_error'] = add_user_to_room(user_to_add, request.user.room)
            return render(request, 'room_detail.html', context)
        else:
            context['error'] = 'Invalid form'
            return render(request, 'room_detail.html', context)
    context['form'] = get_add_user_form()
    return render(request, 'roles.html', context)


def get_roles_forms(room):
    users = User.objects.filter(room=room)
    forms = []
    for user in users:
        try:
            role = Role.objects.get(user=user)
            form = FormUsernameBridge(RoleForm(instance=role), role.user.username)
        except Role.DoesNotExist:
            role = Role(user=user, role='G', room=room)
            role.save()
            form = FormUsernameBridge(RoleForm(role), role.user.username)
        forms.append(form)
    return forms


def parse_forms(request, forms):
    for form in forms:
        user = User.objects.get(username=form.username)
        if  user.pk == int(request.POST['user']):
            role = Role.objects.get(user=user)
            role.role = request.POST['role']
            role.save()


@access('admin')
def update_roles(request, room_id):
    # TODO: improve bd so render can return new data
    #   now site return old roles, but there are updated
    room = Room.objects.get(pk=room_id)
    context = get_context(request)
    context['forms'] = get_roles_forms(room)
    if request.method == 'POST':
        parse_forms(request, context['forms'])
        return render(request, 'roles.html', context)

    return render(request, 'update_roles.html', context)


@access('admin')
def update_role(request, role_id):
    context = get_context(request)
    role = Role.objects.get(pk=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return render(request, 'roles.html', context)
        else:
            context['error'] = 'Form is invalid'
            return render(request, 'update_role.html', context)
    else:
        context['form'] = RoleForm(instance=role)
    return render(request, 'update_role.html', context)