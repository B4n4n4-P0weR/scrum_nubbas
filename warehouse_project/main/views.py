from django.shortcuts import render, redirect
from django.urls import reverse


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
    return render(request, 'report needful stuff.html.html')

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
