from django.shortcuts import render, redirect, HttpResponse
from ..forms import *
from ..models import *

from django.db.models import F
from django.db.models import Sum


def supply_detail(request, supply_number, result=""):
    supply = Supply.objects.get(pk=supply_number)
    supply_content = ContentOfSupply.objects.filter(supplyId=supply_number)
    supply_content_sum = supply_content.aggregate(
        total_price=Sum(F("productId__price") * F("amount"))
    )["total_price"]

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
    shipment_content_sum = shipment_content.aggregate(
        total_price=Sum(F("productId__price") * F("amount"))
    )["total_price"]

    context = {
        "shipment_number": shipment_number,
        "shipment": shipment,
        "shipment_content": shipment_content,
        "sum": shipment_content_sum,
        "result": result,
    }
    return render(request, "shipment one.html", context)


def get_shipment(request):
    shipment_number = request.GET.get("shipment_number")
    return redirect("shipment_detail", shipment_number=shipment_number)


def sale_detail(request, sale_number):
    context = {"sale_number": sale_number}
    return render(request, "sale one.html", context)


def get_sale(request):
    sale_number = request.GET.get("sale_number")
    return redirect("sale_detail", sale_number=sale_number)
