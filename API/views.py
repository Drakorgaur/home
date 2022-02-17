from django.shortcuts import render
from .serializers import *
from welcome.models import User
from home.modules.finance.models import DebtWallet, Debt, Repay
from home.models import Room
from django.http import HttpResponse, JsonResponse


def users_API(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


def user_id_API(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)


def user_username_API(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False)


def rooms_API(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return JsonResponse(serializer.data, safe=False)


def room_id_API(request, pk):
    room = Room.objects.get(pk=pk)
    serializer = RoomSerializer(room)
    return JsonResponse(serializer.data, safe=False)


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
    repay = Repay.objects.get(pk=pk)
    serializer = RepaySerializer(repay, many=False)
    return JsonResponse(serializer.data, safe=False)


def shops_API():
    pass


def shop_by_id(request, pk):
    pass
