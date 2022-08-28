from django.db import models
from django.contrib.auth.models import User


class Truck(models.Model):

    plate_num = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
