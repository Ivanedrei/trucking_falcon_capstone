from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):

    address = models.CharField()
