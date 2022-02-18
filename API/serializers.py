from rest_framework import serializers
from welcome.models import User
from home.models import Room
from home.modules.finance.models import Debt, DebtWallet, Repay, Shop, Product, ToBuy, Bought

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RoomSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField('get_users')

    def get_users(self, room):
        users = User.objects.filter(room=room)
        ret = list()
        for user in users:
            ret.append(user.username)
        return ret

    class Meta:
        model = Room
        fields = ('id', 'name', 'users')


class DebtWalletSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')

    def get_user(self, debt_wallet):
        return debt_wallet.user.username

    class Meta:
        model = DebtWallet
        fields = '__all__'


class DebtSerializer(serializers.ModelSerializer):
    wallet = serializers.SerializerMethodField('get_wallet')
    repay = serializers.SerializerMethodField('get_repays')
    debtor = serializers.SerializerMethodField('get_debtor')
    creator = serializers.SerializerMethodField('get_creator')

    def get_repays(self, debt):
        repays = Repay.objects.filter(debt=debt)
        ret = dict()
        for repay in repays:
            creator = repay.creator
            ret[repay.pk] = {'amount':repay.amount,
                             'description':repay.description,
                             'creator': {
                                 'username': creator.username,
                                 'id': creator.pk,
                             }}
        return ret

    def get_creator(self, debt):
        return debt.creator.username

    def get_debtor(self, debt):
        return debt.debtor.username

    def get_wallet(self, debt):
        return debt.wallet.user.username

    class Meta:
        model = Debt
        fields = '__all__'


class RepaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repay
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ToBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToBuy
        fields = '__all__'


class BoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bought
        fields = '__all__'