from datetime import datetime
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=255, default='')
    manufacturer = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.title} {self.manufacturer}"


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saleDate = models.DateTimeField()


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    director = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return self.title


class Supply(models.Model):
    id = models.AutoField(primary_key=True)
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(default=datetime.now)
    receivingDate = models.DateTimeField(null=True)


class ContentOfSupply(models.Model):
    id = models.AutoField(primary_key=True)
    supplyId = models.ForeignKey(Supply, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)


class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    shipDate = models.DateTimeField()


class ContentOfShipment(models.Model):
    id = models.AutoField(primary_key=True)
    shipmentId = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class ProductsInStock(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    warehouse = models.BooleanField(default=False)
