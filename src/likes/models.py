from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Like(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
