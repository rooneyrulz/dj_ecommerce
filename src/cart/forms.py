from django import forms
from .models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['stocks']

    def clean_stocks(self, *args, **kwargs):
        stocks = self.cleaned_data.get('stocks')
        if int(stocks) < 1:
            raise forms.ValidationError('Please choose the right stock value!')
        else:
            return stocks
