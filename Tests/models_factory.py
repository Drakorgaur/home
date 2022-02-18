import logging
import factory
import faker
from welcome.models import User
from home.modules.finance.models import DebtWallet, Debt, Repay, Shop, RoomProduct, ToBuy, Bought
from home.models import Room
from pytest_factoryboy import register
from django.contrib.auth.hashers import make_password

from home.views import init_room


class RoomFactory(factory.Factory):
    name = factory.Faker('word')

    class Meta:
        model = Room


class UserFactory(factory.Factory):
    username = factory.Faker('first_name')
    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('random'))

    class Meta:
        model = User


class DebtWalletFactory(factory.Factory):
    class Meta:
        model = DebtWallet


class DebtFactory(factory.Factory):
    amount = factory.Faker('pyfloat', positive=True)

    class Meta:
        model = Debt


class RepayFactory(factory.Factory):
    amount = 10.5

    class Meta:
        model = Repay


class ShopFactory(factory.Factory):
    name = factory.Faker('word')
    class Meta:
        model = Shop


class RoomProductFactory(factory.Factory):
    name = factory.Faker('word')
    cost = factory.Faker('pyfloat', positive=True)
    per_kg = factory.Faker('boolean')
    category = 'ot'
    class Meta:
        model = RoomProduct


class ToBuyFactory(factory.Factory):
    cost = factory.Faker('pyfloat', positive=True)
    active = 1
    class Meta:
        model = ToBuy


class BoughtFactory(factory.Factory):
    date = factory.Faker('date')
    cost = factory.Faker('pyfloat', positive=True)

    class Meta:
        model = Bought
