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

    path('debt/to/<str:username>', debt_by_wallet_API, name="debt_by_wallet"),
    path('debt/from/<str:username>', debt_by_debtor_API, name="debt_by_debtor"),

    path('repay/<int:pk>', repay_by_id_API, name="repay_by_id"),

    path('shops', shops_API, name="shops"),
    path('shop/<int:pk>', shop_by_id_API, name="shop_by_id"),

    path('products', products_API, name="products"),
    path('product/<int:pk>', product_by_id_API, name="product_by_id"),

    path('tobuy/<int:pk>', tobuy_by_id_API, name="tobuy_by_id"),
    path('tobuy/creator/<str:username>', tobuy_by_creator_API, name="tobuy_by_creator"),

    path('bought/<int:pk>', bought_by_id_API, name="bought_by_id"),
    path('bought/creator/<str:username>', bought_by_creator_API, name="bought_by_creator"),

]