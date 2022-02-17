import pytest
from Tests.models_factory import RoomFactory
from pytest_factoryboy import register

register(RoomFactory)

@pytest.mark.django_db
def test_ensureRoomCanBeCreated(room):
    room.save()
    assert room.name is not None
