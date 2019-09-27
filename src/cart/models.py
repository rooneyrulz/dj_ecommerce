from django.conf import settings
from django.db import models

from products.models import Product


class Cart(models.Model):
    product = models.OneToOneField(
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
