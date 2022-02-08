from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='roles'),
    path('update/<int:role_id>', update_role, name='update_role'),
    path('update/all/<int:room_id>', update_roles, name='update_roles'),
]


urlpatterns += [
    path('test', test, name='test'),
]
