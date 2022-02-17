from django.shortcuts import render
from .forms import CreateRoomForm
from home.modules.finance.models import DebtWallet
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from welcome.models import User
from django.http import HttpResponse
from home.Helpers.room import *
from home.modules.roles.models import Role
from .models import Room


def index(request):
    context = dict()
    context['user'] = request.user
    context['active'] = 'home'
    user = request.user
    if user.room is not None:
        return render(request, 'main.html', context)
    return render(request, 'main.html', context)


def create_room(request):
    user = request.user
    if user.room is not None:
        # TODO: HttpResponse->render
        return HttpResponse('[Create Room] Not allowed /home/zorgaur/barzali/home/views.py:30')
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            init_room(room, user)
            return redirect("lobby", pk=room.id)
        else:
            return render(request, 'room_create.html', {'error': 'form is invalid',
                                                        'form': form,
                                                        'active': 'room'})
    else:
        form = CreateRoomForm()
        return render(request, 'room_create.html',  {'form': form,
                                                     'active': 'room'})


def init_room(room, user):
    user.room = room
    user.save()

    room.link = get_code()
    room.save()

    user_wallet = DebtWallet(user=user)
    user_wallet.save()

    role = Role(user=user, role='A', room=room)
    role.save()


def init_user_in_room(user, room):
    role = Role(user=user, room=room, role='G')
    role.save()

    user_wallet = DebtWallet(user=user)
    user_wallet.save()


def invite_link_adding(request, code):
    room = Room.objects.get(link=code)
    request.user.room = room
    request.user.save()

    init_user_in_room(request.user, room)

    return redirect('lobby', pk=room.pk)


class Lobby(DetailView):
    model = Room

    # TODO: refactor to DISPATCH(wait for vue.js)
    def dispatch(self, request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs['pk'])
        users = User.objects.filter(room=room)

        context = get_context(request)
        context['active'] = 'room'
        context['users'] = users
        # TODO: create render 404
        if request.user not in users:
            return HttpResponse('[Lobby.dispatch] Not allowed /home/zorgaur/barzali/home/views.py:59')
        return render(request, 'room_detail.html', context)
