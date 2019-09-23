from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stocks', 'added_at']


admin.site.register(Cart, CartAdmin)
