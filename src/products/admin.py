from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'provide_by', 'published_at']


admin.site.register(Product, ProductAdmin)
