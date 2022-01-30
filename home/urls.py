from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path(r'room/create/', create_room, name='create_room'),
    path(r'room/<int:pk>/', Lobby.as_view(), name='lobby'),
]