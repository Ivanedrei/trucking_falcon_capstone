from django.db import models


class PermissionType(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    permission = models.CharField(max_length=15)
