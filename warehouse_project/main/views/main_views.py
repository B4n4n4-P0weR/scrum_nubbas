from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def home(request):
    return render(request, "home.html")

# vr 1
def sales(request):
    return render(request, "sales.html")


def supplies(request):
    return render(request, "supplies.html")


def reports(request):
    return render(request, "reports.html")

# vr 2
def seller(request):
    return render(request, "seller.html")


def manager(request):
    return render(request, "manager.html")


def storekeeper(request):
    return render(request, "storekeeper.html")


def search(request, search_type):
    context = {
        "search_type": search_type,
        "back_url": search_type,  # Добавлено, чтобы передавать URL возврата
    }
    return render(request, "search.html", context)
