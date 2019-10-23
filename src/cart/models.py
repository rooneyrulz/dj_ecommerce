from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import models

from products.models import Product


class CartManager(models.Manager):
    def get_user_item(self, request_user, *args, **kwargs):
        return self.filter(user=request_user)

    def get_cart_item(self, product, user, *args, **kwargs):
        return self.get(product=product, user=user)


class Cart(models.Model):
    product = models.ForeignKey(
        Product,
        default=1,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    stocks = models.IntegerField(
        default=1
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = CartManager()
