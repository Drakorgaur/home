import pytest
from faker import Faker
from welcome.models import User
from Tests.models_factory import UserFactory, RoomFactory
from Tests.helpers import get_room_with_user
from pytest_factoryboy import register
from django.urls import reverse

faker = Faker()


register(UserFactory)
register(RoomFactory)
pytestmark = pytest.mark.django_db


def test_RoomCanBeCreatedByPostRequest(client, user):
    user.save()

    client.login(username=user.username, password='random')

    room_name = faker.word()
    response = client.post(reverse('create_room'), {'name': room_name})
    assert response.status_code == 302

    api_response = client.get(reverse('room_name', kwargs={'name': room_name}))
    assert api_response.status_code == 200
    assert room_name in api_response.content.decode(api_response.charset)


def test_UserCanBeInvitedToRoom(client):
    room, user = get_room_with_user(linked=False)

    client.login(username=user.username, password='random')

    response = client.get(reverse('invite_by_link', kwargs={'code':room.link}))
    assert response.status_code == 302

    response = client.get(reverse('room_name', kwargs={'name':room.name}))
    assert response.status_code == 200

    assert room.name, user.username in response.content


def test_LobbyIsWorkingWell(client):
    room, user = get_room_with_user()

    client.login(username=user.username, password='random')

    response = client.get(reverse('lobby', kwargs={'pk':room.pk}))
    assert response.status_code == 200

    assert room.name, user.username in response.content


