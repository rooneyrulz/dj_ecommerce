from django.conf import settings
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'password', 'password2']
