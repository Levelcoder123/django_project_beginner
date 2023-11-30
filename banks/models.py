from django.db import models


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=80)
    branch = models.CharField(max_length=100)
    services = models.TextField()
    is_islamic = models.BooleanField()
