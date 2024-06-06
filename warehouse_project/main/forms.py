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
    productID = forms.ModelChoiceField(queryset=ProductsInStock.objects.filter(warehouse=False))
    
    class Meta:
        model = Sale
        fields = ["amount"]
        labels = {
            "amount": "Количество",
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["title", "phone", "address", "director"]
        labels = {
            "title": "Наименование",
            "phone": "Телефон",
            "address": "Адрес",
            "director": "Руководитель"
        }

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supplierId"]
        labels = {
            "supplierId": "Поставщик"
        }

class ContentOfSupplyForm(forms.ModelForm):
    class Meta:
        model = ContentOfSupply
        fields = ["productId", "amount"]
        labels = {
            "productId": "Товар",
            "amount": "Количество"
        }

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["shipDate"]
        labels = {
            "shipDate": "Дата отгрузки"
        }

class ContentOfShipmentForm(forms.ModelForm):
    class Meta:
        model = ContentOfShipment
        fields = ["shipmentId", "productId", "amount"]
        labels = {
            "shipmentId": "Id отгрузки",
            "productId": "Id продукта",
            "amount": "Количество"
        }


class ProductsInStockForm(forms.ModelForm):
        class Meta:
            model = ProductsInStock
            fields = ["productId", "amount", "warehouse"]
            labels = {
                "productId": "Id продукта",
                "amount": "Количество",
                "saleDate": "Id расположения"
            }

