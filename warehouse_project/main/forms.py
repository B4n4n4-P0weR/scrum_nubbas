from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["code", "name", "manufacturer", "price"]
        labels = {
            "code": "Артикул",
            "name": "Наименование",
            "manufacturer": "Производитель",
            "price": "Цена",
        }
