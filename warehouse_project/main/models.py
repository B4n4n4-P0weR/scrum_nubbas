from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=50, default='', unique=True)
    title = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    manufacturer = models.CharField(max_length=255, default='')

#class contentOfSale(models.Model):


#class contentOfSupply(models.Model):


#class supplier(models.Model):


class Sale(models.Model):
    code = models.CharField(max_length=50, default='', unique=True)
    saleDate = models.DateTimeField()
    extraInfo = models.CharField(max_length=255, default='')
    #contentOfSale = models.ForeignKey(contentOfSale, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Supply(models.Model):
    code = models.CharField(max_length=50, default='', unique=True)
    #supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    #supplyStatus = models.CharField(max_length=50, default='')
    orderDate = models.DateTimeField()
    receivingDate = models.DateTimeField()
    extraInfo = models.CharField(max_length=255, default='')
    #contentOfSupply = models.ForeignKey(contentOfSupply, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
