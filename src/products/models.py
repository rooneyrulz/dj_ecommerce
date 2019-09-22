from django.conf import settings
from django.db import models
from django.urls import reverse

class Product(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=1000, decimal_places=2)
  description = models.TextField(default="It's awesome product..")
  published_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='product_images')

  def __str__(self):
    return self.name

  def get_absolute_url(self, *args, **kwargs):
    return reverse('products:product_details_view', kwargs={'pk':self.id})

  def get_edit_url(self, *args, **kwargs):
    return reverse('products:product_update_view', kwargs={'pk':self.id})

  
  def get_add_to_cart_url(self, *args, **kwargs):
    return reverse('products:product_add_to_cart_view', kwargs={'pk':self.id})
