from django import forms
from .models import Product
from cart.models import Cart


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['stocks']
