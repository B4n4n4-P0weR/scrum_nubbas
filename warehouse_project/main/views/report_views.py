from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def report_needful_stuff(request):
    return render(request, 'report needful stuff.html')


def report_sold_stuff(request):
    return render(request, 'report sold stuff.html')


def report_stored_stuff(request):
    productsInStock = ProductsInStock.objects.filter(warehouse=True)
    return render(request, 'report stored stuff.html', {'productsInStock': productsInStock})