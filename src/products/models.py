from django.db import models
from django.urls import reverse
from django.conf import settings


class Product(models.Model):
    name = models.CharField(
      max_length=100
    )
    price = models.DecimalField(
      max_digits=1000,
      decimal_places=2
    )
    description = models.TextField(
      default="It's awesome product..",
      blank=True,
      null=True
    )
    provide_by = models.CharField(
      max_length=120,
      default='King Pro Pvt Ltd'
    )
    published_at = models.DateTimeField(
      auto_now_add=True
    )
    image = models.ImageField(
      upload_to='product_images'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse(
          'products:product_details_view',
          kwargs={'pk': self.id}
        )

    def get_edit_url(self, *args, **kwargs):
        return reverse(
          'products:product_update_view',
          kwargs={'pk': self.id}
        )

    def get_like_url(self, *args, **kwargs):
        return reverse(
          'products:product_like_view',
          kwargs={'pk': self.id}
        )

    def get_unlike_url(self, *args, **kwargs):
        return reverse(
          'products:product_unlike_view',
          kwargs={'pk': self.id}
        )

    def get_add_to_cart_url(self, *args, **kwargs):
        return reverse(
          'products:product_add_to_cart_view',
          kwargs={'pk': self.id}
        )

class LikeManager(models.Manager):
  def get_like(self, user, product, *args, **kwargs):
    return self.filter(user=user, product=product)

  def create_like(self, user, product, *args, **kwargs):
    like = self.create(user=user, product=product)
    return like.save()

class Like(models.Model):
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      default=1,
      on_delete=models.CASCADE
    )
    product = models.ForeignKey(
      Product,
      default=1,
      on_delete=models.CASCADE
    )
    liked_at = models.DateTimeField(
      auto_now_add=True
    )

    objects = LikeManager()
