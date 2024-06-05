from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def home(request):
    return render(request, "home.html")


def sales(request):
    return render(request, "sales.html")


def supplies(request):
    return render(request, "supplies.html")


def reports(request):
    return render(request, "reports.html")


def search(request, search_type):
    context = {
        "search_type": search_type,
        "back_url": search_type,  # Добавлено, чтобы передавать URL возврата
    }
    return render(request, "search.html", context)
