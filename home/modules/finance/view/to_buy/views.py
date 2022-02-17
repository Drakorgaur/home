from ...models import ToBuy, Shop, Debt, DebtWallet, Bought
from .forms import ToBuyForm, ShopForm
from ..views import *
from django.http.response import HttpResponse
from .serializers import *
from django.core import serializers
import json
from home.modules.finance.views import create_debt, get_wallet
from datetime import date


def boughts(request):
    context = get_context(request)
    archive = Bought.objects.all()
    context['boughts'] = archive
    return render(request, 'bought/bought.html', context)


def add_tobuy(request):
    context = get_context(request)
    productsJSON = dict()
    for product in RoomProduct.objects.filter(room=request.user.room):
        productsJSON[product.name] = {
            'name': product.name,
            'id': product.id,
            'per_kg': product.per_kg,
            }
    context['productsJSON'] = productsJSON
    if request.method == 'POST':
        weight = request.POST.get('weight', '')
        if weight == '':
            weight = None
        product_id = request.POST.get('product', '')
        product = RoomProduct.objects.get(pk=product_id)
        if weight:
            cost = product.cost * int(weight) / 1000
        else:
            cost = product.cost
        obj = ToBuy(product_id=product_id,
                    shop_id=request.POST.get('shop', ''),
                    weight=weight,
                    creator=request.user,
                    cost=cost,
                    room=request.user.room,
                    active = True)
        obj.save()
        return redirect(tobuy_list)
    form = ToBuyForm()
    context['form'] = form
    return render(request, 'tobuy/add_tobuy.html', context)


def edit_tobuy(request, pk):
    return common_edit(request=request,
                       _class=ToBuy,
                       pk=pk,
                       _form=ToBuyForm,
                       url='tobuy_list',
                       template='tobuy/edit_tobuy.html',
                       link=True)

from django.db.models import Q

def tobuy_list(request):
    if request.method == 'GET' and 'shop' in request.GET:
        return redirect('shopping/{}'.format(request.GET.get('shop', '')))
    else:
        context = dict()
        context['room'] = Room.objects.get(user=request.user)
        tobuys = ToBuy.objects.filter(Q(room=context['room']) & Q(active=True))
        context['tobuys'] = tobuys
        return render(request, 'tobuy/tobuy_list.html', context)


def delete_tobuy(request, pk):
    return common_delete(request=request,
                         _class=ToBuy,
                         pk=pk,
                         redirect_to='tobuy_list')


def create_debts(data, request):
    now = date.today()

    users = User.objects.filter(room=request.user.room)
    amount_users = users.count()

    for element in data:
        if data[element]['debtor'] == request.user.username:
            continue

        product = (ToBuy.objects.get(pk=int(element))).product.name
        data[element]['description'] = f'[{now.strftime("%d/%m/%Y")}] {product} bought by {request.user.username}'
        if data[element]['debtor'] == 0:
            amount = data[element]['amount'] / amount_users
            for user in users:
                if user.username == request.user.username:
                    continue
                debt = Debt(
                    wallet=DebtWallet.objects.get(user=request.user),
                    debtor=user,
                    amount=amount,
                    description=data[element]['description'],
                    creator=request.user
                )
                debt.save()
        else:
            amount = data[element]['amount']
            debt = Debt(
                wallet=DebtWallet.objects.get(user=request.user),
                debtor=User.objects.get(username=data[element]['debtor']),
                amount=amount,
                description=data[element]['description'],
                creator=request.user
            )
            debt.save()


def save_bought(data, user):
    now = date.today()
    total = 0.0
    for product in data:
        total += data[product]['amount']
    bought = Bought(
        date=now.strftime("%Y-%m-%d"),
        receipt=data,
        cost=total,
        buyer=user,
        room=user.room,
    )
    bought.save()

def remove_tobuys(data, disable=False):
    for product in data:
        tobuy = ToBuy.objects.get(pk=int(product))
        if not disable:
            tobuy.delete()
        else:
            tobuy.active = False

def buying_mode(request):
    if request.method == 'POST':
        data = request.POST.get('ids', '')
        data = json.loads(data)
        create_debts(data, request)
        save_bought(data, request.user)
        remove_tobuys(data)
        return redirect('finance')
    context = dict()
    products = ToBuy.objects.filter(Q(room=request.user.room) & Q(active=True))
    users = User.objects.filter(room=request.user.room)
    usersJSON = dict()
    usersJSON['users'] = list()
    for user in users:
        usersJSON['users'].append(user.username)
    context['usersJSON'] = [usersJSON]
    context['products'] = products
    context['productsJSON'] = ToBuySerializer(products, many=True).data

    return render(request, 'tobuy/buying_mode.html', context)