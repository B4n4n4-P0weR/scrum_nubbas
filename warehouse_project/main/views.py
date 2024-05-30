from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .forms import *
from .models import *


def home(request):
    return render(request, 'home.html')


def sales(request):
    return render(request, 'sales.html')


def supplies(request):
    return render(request, 'supplies.html')


def search(request, search_type):
    context = {
        'search_type': search_type,
        'back_url': search_type,  # Добавлено, чтобы передавать URL возврата
    }
    return render(request, 'search.html', context)


def reports(request):
    return render(request, 'reports.html')


def report_needful_stuff(request):
    return render(request, 'report needful stuff.html')


def report_sold_stuff(request):
    return render(request, 'report sold stuff.html')


def report_stored_stuff(request):
    return render(request, 'report stored stuff.html')


def supply_detail(request, supply_number):
    context = {'supply_number': supply_number}
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


def sales_list(request):
    return render(request, 'sales list.html')


def supplies_list(request):
    return render(request, 'supplies list.html')


def sales_add(request):
    return render(request, 'sales add.html')


def supplies_add(request):
    return render(request, 'supplies add.html')


def supplier_requests(request):
    return render(request, 'supplier requests.html')


def supplier_request_add(request):
    return render(request, 'supplier request add.html')


def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'product_list.html', {'products': products})


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

    return render(request, 'product_add.html', {'form': form, 'result': result})


def sale_add(request):
    result = None

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['code']} - {form.cleaned_data['totalPrice']} руб."
            form = SaleForm()
    else:
        form = SaleForm()

    return render(request, 'sales add.html', {'form': form, 'result': result})


def supply_add(request):
    result = None

    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            result = f"Добавлено: {form.cleaned_data['code']} - {form.cleaned_data['totalPrice']} руб."
            form = SupplyForm()
    else:
        form = SupplyForm()

    return render(request, 'supplies add.html', {'form': form, 'result': result})


#Для дебага
def debug_deleted(request):
    return render(request, 'debug delete.html')


def product_clear(request):
    Product.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/supplies/' class='red'>Назад</a> Все продукты удалены")


def sale_clear(request):
    Sale.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/supplies/' class='red'>Назад</a> Все продажи удалены")


def supply_clear(request):
    Supply.objects.all().delete()
    return HttpResponse("<a href='http://127.0.0.1:8000/supplies/' class='red'>Назад</a> Все поставки удалены")
