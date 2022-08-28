from django.db import models
from truckingfalconapi.models.truck import Truck


class Fuel(models.Model):

    fuel_price = models.FloatField()
    gallons_fuel = models.FloatField()
    fuel_date = models.DateField()
    plate_num_id = models.OneToOneField(Truck, on_delete=models.CASCADE)
    total_fuel_cost = models.FloatField()
