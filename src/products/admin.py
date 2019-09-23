from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'published_at']


admin.site.register(Product, ProductAdmin)
