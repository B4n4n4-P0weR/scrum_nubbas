from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def debug_deleted(request):
    return render(request, 'debug delete.html')


def all_clear(request):
    Product.objects.all().delete()
    Sale.objects.all().delete()
    Supplier.objects.all().delete()
    Supply.objects.all().delete()
    ContentOfSupply.objects.all().delete()
    Shipment.objects.all().delete()
    ContentOfShipment.objects.all().delete()
    ProductsInStock.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Всё удалено")


def product_clear(request):
    Product.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Все продукты удалены")


def sale_clear(request):
    Sale.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Все продажи удалены")


def supplier_clear(request):
    Supplier.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Удалено")


def supply_clear(request):
    Supply.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Все поставки удалены")


def content_of_supply_clear(request):
    ContentOfSupply.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Удалено")


def shipment_clear(request):
    Shipment.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Удалено")


def content_of_shipment_clear(request):
    ContentOfShipment.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Удалено")


def sale_contents_show(request):
    contents = SaleContent.objects.all()
    s = ""
    for i in contents:
        s += f"{i.product}\t{i.price_one}\t{i.amount}<br>"
    return HttpResponse(s)