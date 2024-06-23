from datetime import timedelta
from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ #"code", 
            "title", "manufacturer", "price"]
        labels = {
            #"code": "Артикул",
            "title": "Наименование",
            "manufacturer": "Производитель",
            "price": "Цена продаж",
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["saleDate"]
        labels = {"saleDate": "Дата и время продажи"}


class SaleContentForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(productsinstock__warehouse=False).distinct(),
        label="Товар",
    )

    class Meta:
        model = SaleContent
        fields = ["product", "amount"]
        labels = {"amount": "Количество"}


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["title", "phone", "address", "director"]
        labels = {
            "title": "Наименование",
            "phone": "Телефон",
            "address": "Адрес",
            "director": "Руководитель",
        }


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supplierId"]
        labels = {"supplierId": "Поставщик"}


class ContentOfSupplyForm(forms.ModelForm):
    class Meta:
        model = ContentOfSupply
        fields = ["productId", "amount", "price_one"]
        labels = {
            "productId": "Товар",
            "amount": "Количество",
            "price_one": "Цена за шт.",
        }


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = []


class ContentOfShipmentForm(forms.ModelForm):
    class Meta:
        model = ContentOfShipment
        fields = ["productId", "amount"]
        labels = {"productId": "Id продукта", "amount": "Количество"}


class ProductsInStockForm(forms.ModelForm):
    class Meta:
        model = ProductsInStock
        fields = ["productId", "amount", "warehouse"]
        labels = {
            "productId": "Id продукта",
            "amount": "Количество",
            "warehouse": "На складе",  # BooleanField
        }


class SoldReportForm(forms.Form):
    start_date = forms.DateTimeField(required=False, label="С", initial=datetime.now() - timedelta(days=30))
    end_date = forms.DateTimeField(required=False, label="До", initial=datetime.now())