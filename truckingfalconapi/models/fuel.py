from django.db import models
from truckingfalconapi.models.delivery import Delivery


class Fuel(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    delivery_id = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    fuel_price = models.FloatField()
    gallons_fuel = models.FloatField()
    fuel_date = models.DateField()
    total_fuel_cost = models.FloatField()
