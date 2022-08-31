from dataclasses import fields
from django.db import models
from truckingfalconapi.models.employee import Employee


class Delivery(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_address = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    start_date = models.DateField()
    loaded = models.BooleanField()
    total_miles = models.FloatField()
    truck_id = models.IntegerField()
    finish_date = models.DateTimeField()

# finish up the functions input for each of the fields, then check back with Leigha Saturday
