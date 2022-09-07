from django.db import models
from .delivery import Delivery


class Fuel(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    fuel_price = models.DecimalField(max_digits=7, decimal_places=4)
    gallons_fuel = models.DecimalField(max_digits=8, decimal_places=4)
    fuel_date = models.DateTimeField(auto_now_add=True)
    total_fuel_cost = models.DecimalField(max_digits=7, decimal_places=3)
