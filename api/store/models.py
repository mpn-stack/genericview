from django.db import models
from django.utils import timezone


class Product (models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateTimeField()
    register_date = models.DateTimeField(default=timezone.now)

