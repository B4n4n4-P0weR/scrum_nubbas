from django.shortcuts import render, HttpResponse
from django.db.models import Sum, OuterRef, Subquery, F
from ..forms import *
from ..models import *


def report_needful_stuff(request):
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    storage_subquery = ProductsInStock.objects.filter(
        productId=OuterRef('product'), warehouse=True).values('amount')[:1]

    report_data = (
        SaleContent.objects
        .filter(sale__saleDate__range=(start_date, end_date))
        .values('product')
        .annotate(
            total_amount=Sum('amount'),
            storage_amount=Subquery(storage_subquery)
        )
        .filter(total_amount__gte=F('storage_amount'))
    )
    for data in report_data:
        product = Product.objects.get(pk=data['product'])
        data['product'] = str(product)
    return render(request, 'report needful stuff.html', {'report_data': report_data})


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
    backurl = request.GET.get('role', '')
    productsInStock = ProductsInStock.objects.filter(warehouse=True)
    context = {
        'bu': backurl,  # Добавлено, чтобы передавать URL возврата
        'productsInStock': productsInStock
    }
    return render(request, 'report stored stuff.html', context)


def report_saleroom_stuff(request):
    productsInStock = ProductsInStock.objects.filter(warehouse=False)
    return render(request, 'report saleroom stuff.html', {'productsInStock': productsInStock})
