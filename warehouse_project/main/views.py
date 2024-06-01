from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .forms import *
from .models import *
from django.forms import formset_factory


def home(request):
    return render(request, 'home.html')


def sales(request):
    return render(request, 'sales.html')


def supplies(request):
    return render(request, 'supplies.html')


# Добавления
def product_add(request):
    result = None

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['title']} - {form.cleaned_data['price']} руб."
            form = ProductForm()
    else:
        form = ProductForm()

    return render(request, 'product add.html', {'form': form, 'result': result})

def sales_add(request):
    result = None

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['productId']} - {form.cleaned_data['saleDate']}"
            form = SaleForm()
    else:
        form = SaleForm()

    return render(request, 'sales add.html', {'form': form, 'result': result})


def supplier_add(request):
    result = None

    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['title']} - {form.cleaned_data['director']}"
            form = SupplierForm()
    else:
        form = SupplierForm()

    return render(request, 'supplier add.html', {'form': form, 'result': result})


def supplies_add(request):
    result = None

    if request.method == 'POST':
        form = SupplyForm(request.POST)
        Formset = formset_factory(ContentOfSupplyForm)
        formset = Formset(request.POST)
        if form.is_valid() and formset.is_valid():
            supply = form.save()
            amount = save_supply_content(formset, supply)
            result = f"Добавлена поставка от {form.cleaned_data['supplierId']} - количество наименований {amount}"
            form = SupplyForm()
            formset = formset_factory(ContentOfSupplyForm)
    else:
        form = SupplyForm()
        formset = formset_factory(ContentOfSupplyForm)

    return render(request, 'supplies add.html', {'form': form, 'result': result, 'formset': formset})


def save_supply_content(formset, supply):
    for form in formset:
        content_of_supply = form.save(commit=False)
        content_of_supply.supplyId = supply
        content_of_supply.save()
    return len(formset)


def supply_collect(request, supply_id):
    supply = Supply.objects.get(pk=supply_id)
    result = "Поставка уже была получена"
    if supply.receivingDate == None:
        supply.receivingDate = datetime.now()
        supply.save()
        location = ProductLocations.objects.get(title='Склад')
    
        for content in ContentOfSupply.objects.filter(supplyId=supply):
            stock = ProductsInStock.objects.get_or_create(productId=content.productId, locationId=location)[0]
            stock.amount += content.amount
            stock.save()
        result = 'Поставка получена'
    
    return supply_detail(request, supply_id, result)
    

def content_of_supply_add(request):
    result = None

    if request.method == 'POST':
        form = ContentOfSupplyForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['supplyId']} - {form.cleaned_data['productId']}"
            form = ContentOfSupplyForm()
    else:
        form = ContentOfSupplyForm()

    return render(request, 'content of supply add.html', {'form': form, 'result': result})


def shipment_add(request):
    result = None

    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['shipDate']}"
            form = ShipmentForm()
    else:
        form = ShipmentForm()

    return render(request, 'shipment add.html', {'form': form, 'result': result})


def content_of_shipment_add(request):
    result = None

    if request.method == 'POST':
        form = ContentOfShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['shipmentId']} - {form.cleaned_data['productId']} руб."
            form = ContentOfShipmentForm()
    else:
        form = ContentOfShipmentForm()

    return render(request, 'content of shipment add.html', {'form': form, 'result': result})


def product_locations_add(request):
    result = None

    if request.method == 'POST':
        form = ProductLocationsForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['title']}"
            form = ProductLocationsForm()
    else:
        form = ProductLocationsForm()

    return render(request, 'product location add.html', {'form': form, 'result': result})


# Списки
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



def content_of_shipment_list(request):
    content_of_shipment = ContentOfShipment.objects.all()
    return render(request, 'content of shipment list.html', {'content_of_shipment': content_of_shipment})


def product_locations_list(request):
    product_locations = ProductLocations.objects.all()
    return render(request, 'product locations list.html', {'product_locations': product_locations})


# Отчёты
def reports(request):
    return render(request, 'reports.html')


def report_needful_stuff(request):
    return render(request, 'report needful stuff.html')


def report_sold_stuff(request):
    return render(request, 'report sold stuff.html')


def report_stored_stuff(request):
    productsInStock = ProductsInStock.objects.filter(locationId__title='Склад')
    return render(request, 'report stored stuff.html', {'productsInStock': productsInStock})


# Поиск
def search(request, search_type):
    context = {
        'search_type': search_type,
        'back_url': search_type,  # Добавлено, чтобы передавать URL возврата
    }
    return render(request, 'search.html', context)

from django.db.models import F
from django.db.models import Sum
def supply_detail(request, supply_number, result=''):
    supply = Supply.objects.get(pk=supply_number)
    supply_content = ContentOfSupply.objects.filter(supplyId=supply_number)
    sum = supply_content.aggregate(total_price=Sum(F('productId__price') * F('amount')))['total_price']
    
    context = {'supply_number': supply_number, "supply": supply, "supply_content": supply_content, "sum": sum, "result": result}
    return render(request, 'supply one.html', context)


def get_supply(request):
    supply_number = request.GET.get('supply_number')
    return redirect('supply_detail', supply_number=supply_number)


def sale_detail(request, sale_number):
    context = {'sale_number': sale_number}
    return render(request, 'sale one.html', context)


def get_sale(request):
    sale_number = request.GET.get('sale_number')
    return redirect('sale_detail', sale_number=sale_number)


# Удаление (для дебага)
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
    ProductLocations.objects.all().delete()
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

def product_locations_clear(request):
    ProductLocations.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Удалено")

def product_locations_clear(request):
    ProductLocations.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/clear'>Назад</a> Все места удалены")
