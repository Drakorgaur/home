from django.shortcuts import render
from .models import Role
from .forms import RoleForm

ц
def get_context(request):
    context = dict()
    context['user'] = request.user
    try:
        roles = Role.objects.filter(room=request.user.room)
    except Role.DoesNotExist:
        context['error'] = 'roles does not exists. Contact moderator to sole this'
        context['roles'] = None
        return context
    context['roles'] = roles
    return context


def index(request):
    roles = Role.objects.filter(room=request.user.room)
    return render(request, 'roles.html', {'user': request.user, 'roles': roles})


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
            return render(request, 'roles.html', context)
    else:
        context['form'] = RoleForm()
    return render(request, 'roles.html', context)