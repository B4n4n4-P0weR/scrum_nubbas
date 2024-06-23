from django.shortcuts import render, HttpResponse
from django.db.models import Sum
from ..forms import *
from ..models import *


def report_needful_stuff(request):
    return render(request, 'report needful stuff.html')


def report_sold_stuff(request):
    if request.method == "POST":
        form = SoldReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            sales_data = (
                SaleContent.objects
                .filter(sale__saleDate__range=(start_date, end_date))
                .values('product')
                .annotate(total_amount=Sum('amount'))
            )
            for data in sales_data:
                product = Product.objects.get(pk=data['product'])
                data['product'] = str(product)
    else:
        form = SoldReportForm()
        sales_data = None
    return render(request, 'report sold stuff.html', {'form': form, 'sales_data': sales_data})


def report_stored_stuff(request):
    productsInStock = ProductsInStock.objects.filter(warehouse=True)
    return render(request, 'report stored stuff.html', {'productsInStock': productsInStock})


def report_saleroom_stuff(request):
    productsInStock = ProductsInStock.objects.filter(warehouse=False)
    return render(request, 'report saleroom stuff.html', {'productsInStock': productsInStock})
