import pytest
from faker import Faker
from Tests.models_factory import UserFactory
from welcome.forms import UserRegistrationForm
from pytest_factoryboy import register
from django.urls import reverse

faker = Faker()

register(UserFactory)
@pytest.mark.django_db
def test_UserRegistrationFormIsWorkingWell(client, user):
    pswd = faker.word()
    new_user = UserRegistrationForm({'username':user.username,
                               'email': user.email,
                               'password': pswd,
                               'password2': pswd})
    new_user = new_user.save()

    assert new_user.username == user.username
    assert new_user.email == user.email

    response = client.get(reverse('user_by_username', kwargs={'username': new_user.username}))
    assert new_user.username in response.content.decode(response.charset)