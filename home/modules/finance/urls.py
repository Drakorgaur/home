from django.urls import path
from .views import *
from .view.shop.views import *
from .view.products.views import *
from .view.to_buy.views import *

urlpatterns = [
    path('', finance_index, name='finance'),
    path('debts/', debts, name='debts'),
    path('debts/add', add_debt, name='add_debt'),
]

urlpatterns += [
    path('debts/repay/add', add_repay, name='add_repay'),
    path('debts/repay/add/<int:debt_id>', add_repay, name='add_repay'),
    path('debts/repay/approve/<int:repay_id>', repay_approve, name='approve_repay'),
    path('debts/repay/decline/<int:repay_id>', repay_decline, name='decline_repay'),
]


urlpatterns += [
    path('shops', shop_list, name='shops_list'),
    path('shop/<int:pk>', shop_detail, name='shop_detail'),
    path('shop/add', add_shop, name='add_shop'),
]


urlpatterns += [
    path('products', product_list, name='products_list'),
    path('product/add', add_product, name='add_product'),
    path('product/edit/<int:pk>', edit_product, name='edit_product'),
]


urlpatterns += [
    path('tobuys', tobuy_list, name='tobuy_list'),
    path('tobuy/add', add_tobuy, name='add_tobuy'),
    path('tobuy/del/<int:pk>', delete_tobuy, name='delete_tobuy'),
    path('tobuy/edit/<int:pk>', edit_tobuy, name='edit_tobuy'),

    path('shopping', buying_mode, name='buying_mode')
]



urlpatterns += [
    path('archive', boughts, name='boughts')
    ]