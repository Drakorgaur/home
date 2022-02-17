import pytest
from faker import Faker
from Tests.models_factory import RoomFactory
from home.forms import CreateRoomForm
from pytest_factoryboy import register

faker = Faker()

register(RoomFactory)
@pytest.mark.django_db
def test_CreateRoomFormIsWorkingWell(client, room):
    room.save()

    obj = CreateRoomForm({'name':room.name})
    saved_object = obj.save()

    assert saved_object.name == room.name

