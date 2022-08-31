from django.db import models


class Truck(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    plate_number = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
