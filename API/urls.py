from django.urls import path
from .views import *

urlpatterns = [
    path('users', users_API, name='users'),
    path('user/<int:pk>', user_id_API, name='user_by_id'),
    path('user/<str:username>', user_username_API, name='user_by_username'),

    path('rooms', rooms_API, name='rooms'),
    path('room/<int:pk>', room_id_API, name='room_id'),
    path('room/<str:name>', room_name_API, name='room_name'),

    path('wallet/<str:username>', wallet_API, name="wallet_name"),

    path('debt/to/<str:username>', debt_by_wallet, name="debt_by_wallet"),
    path('debt/from/<str:username>', debt_by_debtor, name="debt_by_debtor"),

    path('repay/<int:pk>', repay_by_id, name="repay_by_id"),

    path('shop/<int:pk>', shop_by_id, name="shop_by_id"),
]