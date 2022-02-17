from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from welcome.views import login, logout_, register

def index(request):
    return HttpResponse([{'id': request.user.id, 'username':request.user.username} ])

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout_, name='logout'),
    path('register', register, name='register'),
    path('welcome/', include('welcome.urls')),
    path('home/', include('home.urls')),
    path('api/', include('API.urls')),
    path('admin/', admin.site.urls),
    path('site/healthcheck', index),
]
