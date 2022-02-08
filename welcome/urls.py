from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='welcome'),
    path('register', register, name='register')
]