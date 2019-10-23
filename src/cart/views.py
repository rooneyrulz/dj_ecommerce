from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView
from django.contrib import messages

from .models import Cart


# Cart List View
class CartListView(ListView):
    context_object_name = 'products'

    def get_queryset(self):
        return Cart.objects.get_user_item(self.request.user)


# Cart Item Delete View
class CartDeleteView(DeleteView):
    queryset = Cart.objects.all()
    context_object_name = 'product'
    template_name = 'cart/cart_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Product has been removed from cart!')
        return reverse('cart:cart_list_view')
