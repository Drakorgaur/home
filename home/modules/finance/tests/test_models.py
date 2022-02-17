import pytest
from welcome.models import User
from Tests.models_factory import *
from Tests.helpers import get_wallet, get_debt, get_repay
from pytest_factoryboy import register
from django.urls import reverse


register(DebtWalletFactory)
pytestmark = pytest.mark.django_db

def test_DebtWalletModelWorks(client):
    """
    @models DebtWallet
    """
    wallet = get_wallet()

    response = client.get(reverse('wallet_name', kwargs={'username':wallet.user.username}))
    assert wallet.user.username in response.content.decode(response.charset)


def test_DebtModelWorks(client):
    """
    @models Debt
    """
    debt = get_debt()

    response = client.get(reverse('debt_by_debtor', kwargs={'username':debt.debtor.username}))
    content = response.content.decode(response.charset)
    assert debt.debtor.username, debt.creator.username in content
    assert debt.description in content
    assert '\"repay\": {},' in content


def test_RepayModelWorks(client):
    """
    @models Repay
    """
    repay = get_repay()

    response = client.get(reverse('debt_by_debtor', kwargs={'username': repay   .debt.debtor.username}))
    assert repay.debt.description in response.content.decode(response.charset)


def test_ShopModelWorks(client):
    """
    @models Shop
    """
    repay = get_shop()

    response = client.get(reverse('debt_by_debtor', kwargs={'username': repay.debt.debtor.username}))
    assert repay.debt.description in response.content.decode(response.charset)
