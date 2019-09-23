from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Cart


# Cart List View
# @login_required()
def cart_list_view(request):
    products = Cart.objects.filter(user=request.user)
    context = {
        'products': products
    }
    return render(request, 'cart/cart_list.html', context)
