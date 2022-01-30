from django.shortcuts import render
from .forms import CreateRoomForm
from .models import Room
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from welcome.models import User
from django.http import HttpResponse

def index(request):
    user = request.user
    if user.room is not None:
        return render(request, 'main.html', {'user': request.user,
                                             'active': 'home'})
    return render(request, 'main.html', {'username': request.user.username,
                                         'href': 'room/create/',
                                         'active': 'home'})

def create_room(request):
    user = request.user
    if user.room is not None:
        # TODO: HttpResponse->render
        return HttpResponse('Not allowed')
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=True)
            return redirect("/room?id={}".format(room.id))
        else:
            return render(request, 'room_create.html', {'error': 'form is invalid',
                                                        'form': form,
                                                        'active': 'room'})
    else:
        form = CreateRoomForm()
        return render(request, 'room_create.html',  {'form': form,
                                                     'active': 'room'})

class Lobby(DetailView):
    model = Room

    # TODO: refactor to DISPATCH(wait for vue.js)
    def dispatch(self, request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs['pk'])
        users = User.objects.filter(room=room)

        # TODO: create render 404
        if request.user not in users:
            return HttpResponse('Not allowed')

        context = dict()
        context['user'] = request.user
        context['active'] = 'room'
        context['users'] = users
        return render(request, 'room_detail.html', context)
