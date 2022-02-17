from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('room/<int:pk>/', Lobby.as_view(), name='lobby'),
    path('room/create/', create_room, name='create_room'),
    path('room/invite/<str:code>/', invite_link_adding, name='invite_by_link'),
    path('finance/', include('home.modules.finance.urls')),
    path('roles/', include('home.modules.roles.urls')),
]