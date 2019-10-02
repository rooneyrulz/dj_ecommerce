from django.contrib import admin

from .models import Product, Like


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'provide_by', 'published_at']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'liked_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Like, LikeAdmin)
