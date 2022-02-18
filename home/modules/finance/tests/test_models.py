import pytest
from welcome.models import User
from Tests.models_factory import *
from Tests.helpers import *
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
    shop = get_shop()
    shop.save()

    response = client.get(reverse('shop_by_id', kwargs={'pk': shop.pk}))
    assert shop.name in response.content.decode(response.charset)


def test_ProductModelWorks(client):
    """
    @model Product
    """
    product = get_product()
    product.save()

    response = client.get('product_by_id', kwargs={'pk': product.pk})
    assert product.name, product.cost in get_body(response)


def test_ToBuyModelWorks(client):
    tobuy = get_tobuy()
    tobuy.save()

    response = client.get('tobuy_by_id', kwargs={'pk': tobuy.pk})
    assert tobuy.product.pk, tobuy.cost in get_body(response)


def test_BoughtModelWorks(client):
    bought = get_bought()
    bought.save()

    response = client.get('bought_by_id', kwargs={'pk': bought.pk})
    assert bought.pk, bought.cost in get_body(response)