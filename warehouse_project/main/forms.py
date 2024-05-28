from django import forms
from .models import Product


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
