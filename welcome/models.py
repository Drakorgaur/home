from django.db import models
from django.contrib.auth.models import AbstractUser
from home.models import Room

class User(AbstractUser):
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

class TokenUser(models.Model):
    token = models.IntegerField(primary_key=True)
    token_exp = models.DateField()

    class Meta:
        abstract = True


class Guest(TokenUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Visitor(TokenUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username