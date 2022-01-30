from django.db import models

class Room(models.Model):
    COLORS = (
        ('#21B6A8', 'blue-green'),
        ('#7EC8E3', 'baby-blue'),
        ('#868B8E', 'grey'),
    )
    name  = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLORS)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
