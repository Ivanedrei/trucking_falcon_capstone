from django.db import models
from truckingfalconapi.models.driver import Driver


class Delivery(models.Model):

    driver_id = models.OneToOneField(Driver, on_delete=models.CASCADE)
    from_address = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    loaded = models.BooleanField()
    total_miles = models.FloatField()
    fuel_id = models.IntegerField()
