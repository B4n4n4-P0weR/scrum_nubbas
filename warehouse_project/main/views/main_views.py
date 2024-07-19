from django.shortcuts import render, HttpResponse
from ..forms import *
from ..models import *


def home(request):
    return render(request, "home.html")


def seller(request):
    return render(request, "seller.html")


def manager(request):
    return render(request, "manager.html")


def storekeeper(request):
    return render(request, "storekeeper.html")
