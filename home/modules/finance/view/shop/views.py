from home.modules.finance.models import Shop
from home.Helpers.room import *
from django.shortcuts import render, redirect
from home.modules.finance.models import RoomProduct
from .forms import ShopForm
from ..views import *

def shop_list(request):
    return common_list(request=request,
                         _class=Shop,
                         template='shop/shops_list.html')


def shop_detail(request, pk):
    return common_detail(request=request,
                         _class=Shop,
                         pk=pk,
                         template='shop/shop_detail.html',
                         _subclass=RoomProduct)


def add_shop(request):
    return common_create(request=request,
                         _class=ShopForm,
                         url='shops_list',
                         template='shop/add_shop.html')