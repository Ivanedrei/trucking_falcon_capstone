from django.db import models
from django.contrib.auth.models import User
from truckingfalconapi.models.truck import Truck


class Driver(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    truck_id = models.OneToOneField(Truck, on_delete=models.CASCADE)
