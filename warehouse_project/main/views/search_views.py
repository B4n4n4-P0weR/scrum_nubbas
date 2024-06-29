from django.shortcuts import render, redirect, HttpResponse
from ..forms import *
from ..models import *

from django.db.models import F
from django.db.models import Sum


def supply_detail(request, supply_number, result=""):
    supply = Supply.objects.get(pk=supply_number)
    supply_content = ContentOfSupply.objects.filter(supplyId=supply_number)

    supply_content_sum = 0
    for content in supply_content:
        supply_content_sum += content.amount * content.price_one

    context = {
        "supply_number": supply_number,
        "supply": supply,
        "supply_content": supply_content,
        "sum": supply_content_sum,
        "result": result,
    }
    return render(request, "supply one.html", context)


def get_supply(request):
    supply_number = request.GET.get("supply_number")
    return redirect("supply_detail", supply_number=supply_number)


def shipment_detail(request, shipment_number, result=""):
    shipment = Shipment.objects.get(pk=shipment_number)
    shipment_content = ContentOfShipment.objects.filter(shipmentId=shipment_number)

    context = {
        "shipment_number": shipment_number,
        "shipment": shipment,
        "shipment_content": shipment_content,
        "result": result,
    }
    return render(request, "shipment one.html", context)


def get_shipment(request):
    shipment_number = request.GET.get("shipment_number")
    return redirect("shipment_detail", shipment_number=shipment_number)


def sale_detail(request, sale_number):
    sale = Sale.objects.get(pk=sale_number)
    sale_contents = SaleContent.objects.filter(sale=sale)
    sale_sum = 0
    for content in sale_contents:
        sale_sum += content.price_one * content.amount
    context = {
        "sale_number": sale_number,
        "sale": sale,
        "sale_contents": sale_contents,
        "total": sale_sum
    }
    return render(request, "sale one.html", context)


def get_sale(request):
    sale_number = request.GET.get("sale_number")
    return redirect("sale_detail", sale_number=sale_number)


def get_product(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(title__icontains=query) | Product.objects.filter(manufacturer__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'product list.html', {'products': products})