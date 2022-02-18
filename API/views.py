from django.shortcuts import render
from .serializers import *
from welcome.models import User
from home.modules.finance.models import DebtWallet, Debt, Repay, ToBuy, Bought, RoomProduct
from home.models import Room
from django.http import HttpResponse, JsonResponse


def API_by_id(_class, pk):
    try:
        objects = _class.objects.get(pk=pk)
    except _class.DoesNotExist:
        return JsonResponse({})
    SerializerClass = globals()[str(_class.__name__) + 'Serializer']
    serializer = SerializerClass(objects)

    return JsonResponse(serializer.data, safe=False)


def API_all(_class):
    try:
        objects = _class.objects.all()
    except _class.DoesNotExist:
        return JsonResponse({})
    SerializerClass = globals()[str(_class.__name__) + 'Serializer']
    serializer = SerializerClass(objects, many=True)
    return JsonResponse(serializer.data, safe=False)


def users_API(request):
    return API_all(User)


def user_id_API(request, pk):
    return API_by_id(User, pk)


def user_username_API(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)


def rooms_API(request):
    return API_all(Room)


def room_id_API(request, pk):
    return API_by_id(Room, pk)


def room_name_API(request, name):
    room = Room.objects.get(name=name)
    serializer = RoomSerializer(room)
    return JsonResponse(serializer.data, safe=False)


def wallet_API(request, username):
    user = User.objects.get(username=username)
    wallet = DebtWallet.objects.get(user=user)
    serializer = DebtWalletSerializer(wallet, many=False)
    return JsonResponse(serializer.data, safe=False)


def debt_by_debtor_API(request, username):
    user = User.objects.get(username=username)
    debts = Debt.objects.filter(debtor=user)
    serializer = DebtSerializer(debts, many=True)
    return JsonResponse(serializer.data, safe=False)


def debt_by_wallet_API(request, username):
    user = User.objects.get(username=username)
    wallet = DebtWallet.objects.get(user=user)
    debts = Debt.objects.filter(wallet=wallet)
    serializer = DebtSerializer(debts, many=True)
    return JsonResponse(serializer.data, safe=False)


def repay_by_id_API(request, pk):
    return API_by_id(Repay, pk)


def shops_API(request):
    return API_all(Shop)


def shop_by_id_API(request, pk):
    return API_by_id(Shop, pk)


def products_API(request):
    return API_all(RoomProduct)


def product_by_id_API(request, pk):
    return API_by_id(RoomProduct, pk)


def tobuy_by_id_API(request, pk):
    return API_by_id(ToBuy, pk)


def tobuy_by_creator_API(request, username):
    user = User.objects.get(username=username)
    tobuys = ToBuy.objects.filter(creator=user)
    serializer = ToBuySerializer(tobuys, many=True)
    return JsonResponse(serializer.data, safe=False)


def bought_by_id_API(request, pk):
    return API_by_id(Bought, pk)


def bought_by_creator_API(request, username):
    user = User.objects.get(username=username)
    tobuys = ToBuy.objects.filter(creator=user)
    serializer = ToBuySerializer(tobuys, many=True)
    return JsonResponse(serializer.data, safe=False)