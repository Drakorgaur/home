import pytest
from faker import Faker
from Tests.models_factory import UserFactory, DebtWalletFactory
from Tests.helpers import get_user, get_debt
from home.modules.finance.forms import DebtForm, RepayForm
from home.modules.finance.models import DebtWallet
from pytest_factoryboy import register
from django.urls import reverse

faker = Faker()

register(DebtWalletFactory)
pytestmark = pytest.mark.django_db


def test_DebtFormIsWorking(client, debt_wallet):
    user = get_user()
    user.save()

    debt_wallet.user = user
    debt_wallet.save()

    form = DebtForm({'description': 'test_DebtFormIsWorking',
                     'debtor': user,
                     'amount': 0})
    # form.is_valid()
    debt = form.save(commit=False)
    debt.wallet_id = debt_wallet.pk
    debt.creator = user
    debt.save()

    response = client.get(reverse('debt_by_debtor', kwargs={'username':user.username}))
    assert user.pk, debt.pk in response.contentdecode(response.charset)

    for field in debt.field_names():
        assert field in response.content.decode(response.charset)


def test_RepayFormWorking(client):
    user = get_user()
    debt = get_debt(owner=user)
    debt.save()

    form = RepayForm({'debt': debt,
                      'amount': 1,
                      'description': 'test_RepayFormWorking'})
    repay = form.save(commit=False)
    repay.creator = user
    repay.save()

    response = client.get(reverse('repay_by_id', kwargs={'pk':repay.pk}))
    content = response.content.decode(response.charset)
    assert user.pk, repay.pk in content

    response = client.get(reverse('debt_by_wallet', kwargs={'username':user.username}))
    content = response.content.decode(response.charset)
    assert debt.description in content
    assert repay.description in content
