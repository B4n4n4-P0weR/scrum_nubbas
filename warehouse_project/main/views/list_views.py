from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product list.html', {'products': products})


def sales_list(request):
    order_by = request.GET.get('order_by', 'desc')
    if order_by == 'asc':
        sales = Sale.objects.all().order_by('-id')
    else:
        sales = Sale.objects.all().order_by('id')
    return render(request, 'sales list.html', {'sales': sales, 'order_by': order_by})


def supplier_list(request):
    supplier = Supplier.objects.all()
    return render(request, 'supplier list.html', {'suppliers': supplier})


def supplies_list(request):
    backurl = request.GET.get('role', '')
    order_by = request.GET.get('order_by', 'desc')
    if order_by == 'asc':
        supplies = Supply.objects.all().order_by('id')
    else:
        supplies = Supply.objects.all().order_by('-id')
    context = {
        'bu': backurl,  # Добавлено, чтобы передавать URL возврата
        'supplies': supplies,
        'order_by': order_by
    }
    return render(request, 'supplies list.html', context)


def shipment_list(request):
    order_by = request.GET.get('order_by', 'desc')
    if order_by == 'asc':
        shipment = Shipment.objects.all().order_by('id')
    else:
        shipment = Shipment.objects.all().order_by('-id')
    return render(request, 'shipment list.html', {'shipments': shipment, 'order_by': order_by})