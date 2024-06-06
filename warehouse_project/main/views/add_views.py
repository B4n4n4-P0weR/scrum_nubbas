from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *
from django.forms import formset_factory
from django.db import transaction


def product_add(request):
    result = None

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['title']} - {form.cleaned_data['price']} руб."
            form = ProductForm()
    else:
        form = ProductForm()

    return render(request, "product add.html", {"form": form, "result": result})


def sales_add(request):
    result = None

    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale: Sale = form.save(commit=False)
            sale.saleDate = datetime.now()

            sale_res, result = sale_possible(sale.productId, sale.amount)

            if sale_res:
                result = f"Продано {sale.amount} шт. {sale.productId}"
                stock = ProductsInStock.objects.get(
                    warehouse=False, productId=sale.productId
                )
                stock.amount -= sale.amount

                with transaction.atomic():
                    sale.save()
                    stock.save()

                form = SaleForm()
    else:
        form = SaleForm()
        products_count = form.fields['productId'].queryset.count()

    return render(request, "sales add.html", {"form": form, "count": products_count, "result": result})


def sale_possible(product: Product, amount: int):
    try:
        stock = ProductsInStock.objects.get(warehouse=False, productId=product)
        if stock.amount < amount:
            result = f"В торговом помещении всего {stock.amount} шт. товара {product}"
            return (False, result)
    except ProductsInStock.DoesNotExist:
        result = f"В торговом помещении нет товара: {product}"
        return (False, result)

    return (True, "Продажа возможна")


def supplier_add(request):
    result = None

    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['title']} - {form.cleaned_data['director']}"
            form = SupplierForm()
    else:
        form = SupplierForm()

    return render(request, "supplier add.html", {"form": form, "result": result})


def supplies_add(request):
    result = None

    if request.method == "POST":
        form = SupplyForm(request.POST)
        Formset = formset_factory(ContentOfSupplyForm)
        formset = Formset(request.POST)
        if form.is_valid() and formset.is_valid():

            with transaction.atomic():
                supply = form.save()
                amount = save_supply_content(formset, supply)

            result = f"Добавлена поставка от {form.cleaned_data['supplierId']} - количество наименований {amount}"
            form = SupplyForm()
            formset = formset_factory(ContentOfSupplyForm)
    else:
        form = SupplyForm()
        formset = formset_factory(ContentOfSupplyForm)

    return render(
        request,
        "supplies add.html",
        {"form": form, "result": result, "formset": formset},
    )


def save_supply_content(formset, supply):
    for form in formset:
        content_of_supply = form.save(commit=False)
        content_of_supply.supplyId = supply
        content_of_supply.save()
    return len(formset)


from .search_views import supply_detail


def supply_collect(request, supply_id):
    supply = Supply.objects.get(pk=supply_id)
    result = "Поставка уже была получена"
    if supply.receivingDate == None:
        supply.receivingDate = datetime.now()
        supply.save()

        for content in ContentOfSupply.objects.filter(supplyId=supply):
            stock = ProductsInStock.objects.get_or_create(productId=content.productId)[
                0
            ]
            stock.amount += content.amount
            stock.save()
        result = "Поставка получена"

    return supply_detail(request, supply_id, result)


def content_of_supply_add(request):
    result = None

    if request.method == "POST":
        form = ContentOfSupplyForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['supplyId']} - {form.cleaned_data['productId']}"
            form = ContentOfSupplyForm()
    else:
        form = ContentOfSupplyForm()

    return render(
        request, "content of supply add.html", {"form": form, "result": result}
    )


def shipment_add(request):
    result = None

    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['shipDate']}"
            form = ShipmentForm()
    else:
        form = ShipmentForm()

    return render(request, "shipment add.html", {"form": form, "result": result})


def content_of_shipment_add(request):
    result = None

    if request.method == "POST":
        form = ContentOfShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['shipmentId']} - {form.cleaned_data['productId']} руб."
            form = ContentOfShipmentForm()
    else:
        form = ContentOfShipmentForm()

    return render(
        request, "content of shipment add.html", {"form": form, "result": result}
    )
