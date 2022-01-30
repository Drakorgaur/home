from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='welcome'),
    path('login', login, name='login'),
    path('register', register, name='register')
]