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
        fields = ["saleDate", "productId", "amount"]
        labels = {
            "saleDate": "Дата продажи",
            "productId": "Id продукта",
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
        fields = ["supplierId", "orderDate", "receivingDate"]
        labels = {
            "supplierId": "Поставщик",
            "orderDate": "Дата заказа",
            "receivingDate": "Дата получения"
        }

class ContentOfSupplyForm(forms.ModelForm):
    class Meta:
        model = ContentOfSupply
        fields = ["supplyId", "productId", "amount"]
        labels = {
            "supplyId": "Id поставки",
            "productId": "Id продукта",
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

class ProductLocationsForm(forms.ModelForm):
    class Meta:
        model = ProductLocations
        fields = ["title"]
        labels = {
            "title": "Наименование (склад/торговое помещение)"
        }

class ProductsInStockForm(forms.ModelForm):
        class Meta:
            model = ProductsInStock
            fields = ["productId", "amount", "locationId"]
            labels = {
                "productId": "Id продукта",
                "amount": "Количество",
                "saleDate": "Id расположения"
            }

