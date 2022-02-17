from django.shortcuts import render
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from .models import User
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login as default_login
from django.shortcuts import redirect
from django.contrib.auth import logout


def index(request):
    return render(request, 'welcome.html', {'h1': 'Welcome', 'p': request.user.id})

# TODO: add returns with err
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Auth.authenticate(Auth(), request=request, username=request.POST['username'],
                                     password=request.POST['password'])
            if user is not None:
                default_login(request, user)
                return redirect('welcome')
    form = LoginForm()
    return render(request, 'login.html', {'form': form } )


def logout_(request):
    logout(request)
    return redirect('welcome')


# TODO: add returns with err
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('welcome')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

class Auth(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as e:
            return None
        if check_password(password, user.password):
            return user
        return None
