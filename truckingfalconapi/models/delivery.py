from django.db import models
from .employee import Employee
from .truck import Truck


class Delivery(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_address = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    loaded = models.BooleanField()
    total_miles = models.FloatField()
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    finish_date = models.DateTimeField(auto_now_add=True)
