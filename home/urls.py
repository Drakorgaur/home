from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('room/create/', create_room, name='create_room'),
    path('room/<int:pk>/', Lobby.as_view(), name='lobby'),
    path('room/invite/<str:code>/', invite_link_adding),
    path('finance/', include('home.modules.finance.urls')),
    path('roles/', include('home.modules.roles.urls')),
]