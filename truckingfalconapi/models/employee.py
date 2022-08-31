from django.db import models
from django.contrib.auth.models import User
from truckingfalconapi.models.permission_type import PermissionType


class Employee(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission_type = models.ForeignKey(
        PermissionType, on_delete=models.CASCADE)
