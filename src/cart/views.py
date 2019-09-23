from django.shortcuts import render

from .models import Cart


# Cart List View
def cart_list_view(request):
    products = Cart.objects.all()
    context = {
        'products': products
    }
    return render(request, 'cart/cart_list.html', context)
