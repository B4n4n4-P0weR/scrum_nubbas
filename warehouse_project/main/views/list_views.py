from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product list.html', {'products': products})


def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales list.html', {'sales': sales})


def supplier_list(request):
    supplier = Supplier.objects.all()
    return render(request, 'supplier list.html', {'suppliers': supplier})


def supplies_list(request):
    supply = Supply.objects.all()
    return render(request, 'supplies list.html', {'supplies': supply})


def shipment_list(request):
    shipment = Shipment.objects.all()
    return render(request, 'shipment list.html', {'shipments': shipment})
