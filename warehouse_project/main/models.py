from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=50, default='', unique=True)
    title = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    manufacturer = models.CharField(max_length=255, default='')
