from django.db import models
from welcome.models import User
from home.models import Room

class Role(models.Model):
    roles = (
        ('A', 'admin'),
        ('I', 'inhabitant'),
        ('G', 'guest'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role_user')
    role = models.CharField(max_length=20, choices=roles)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='role_room')

    def __str__(self):
        return '{} {}'.format(self.role, self.user)