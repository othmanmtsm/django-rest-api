from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField()
    price = models.FloatField()
    capacity = models.IntegerField()
    isAvailable = models.BooleanField()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    img = models.URLField()