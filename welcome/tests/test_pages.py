import pytest
from faker import Faker
from welcome.models import User
from .test_models import UserFactory
from pytest_factoryboy import register

faker = Faker()

register(UserFactory)
pytestmark = pytest.mark.django_db

# -- source
def test_loginPagWorkingWell(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert '<h1>Login</h1>' in response.content.decode(response.charset)


def test_logoutRedirectsCorrectly(client):
    response = client.get('/logout')
    assert response.status_code == 302
    response = client.get(response.url)
    assert '<h1>Welcome</h1>' in response.content.decode(response.charset)


def test_RegistrationPageWorkingWell(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert '<h1>Registration</h1>' in response.content.decode(response.charset)


# -- welcome
def test_UserCanRegister(client):
    passwd = faker.word()
    user = {
        'username': faker.word(),
        'password': passwd,
        'password2': passwd,
        'email': faker.email(),
    }
    response = client.post('/register', user)
    assert response.status_code == 302
    response = client.get('/api/users')
    assert user['username'] in response.content.decode(response.charset)


def test_UserCanLoginAndLogout(client, user):
    user.save()

    response = client.get('/api/users')
    assert user.username in response.content.decode(response.charset)

    response = client.post('/login', {'username': user.username,
                                      'password': 'random'})
    assert response.status_code == 302

    response = client.get('/site/healthcheck')
    assert user.username, user.pk in response.content.decode(response.charset)


    client.get('/logout')
    response = client.get('/site/healthcheck')
    assert user.username, user.pk not in response.content.decode(response.charset)

