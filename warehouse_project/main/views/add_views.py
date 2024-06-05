from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *
from django.forms import formset_factory


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
    
        for content in ContentOfSupply.objects.filter(supplyId=supply):
            stock = ProductsInStock.objects.get_or_create(productId=content.productId)[0]
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
