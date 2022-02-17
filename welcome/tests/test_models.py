import pytest
from welcome.models import User
from Tests.models_factory import UserFactory, RoomFactory
from pytest_factoryboy import register

register(UserFactory)
register(RoomFactory)

def test_ensureUserCreatesAndRoomCanBeAttached(user, room):
    user.room = room
    assert user is not None
    assert  user.room is not None

