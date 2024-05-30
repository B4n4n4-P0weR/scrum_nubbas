from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["code", "title", "manufacturer", "price"]
        labels = {
            "code": "Артикул",
            "title": "Наименование",
            "manufacturer": "Производитель",
            "price": "Цена",
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["code", "saleDate", "extraInfo", "totalPrice"]
        labels = {
            "code": "Артикул",
            "saleDate": "Дата продажи",
            "extraInfo": "Доп. Информация",
            "totalPrice": "Сумма продажи",
        }


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["code", "orderDate", "receivingDate", "extraInfo", "totalPrice"]
        labels = {
            "code": "Артикул",
            "orderDate": "Дата заказа",
            "receivingDate": "Дата получения",
            "extraInfo": "Доп. Информация",
            "totalPrice": "Сумма поставки",
        }
