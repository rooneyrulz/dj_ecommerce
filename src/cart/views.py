from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cart


# Cart List View
@login_required()
def cart_list_view(request):
    products = Cart.objects.filter(user=request.user)
    context = {
        'cart_item_count': len(products),
        'products': products
    }
    return render(request, 'cart/cart_list.html', context)


# Delete Cart Item
@login_required()
def cart_item_delete_view(request, pk):
    product = get_object_or_404(Cart, id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product has been removed from the cart!')
        return redirect('/cart')
    context = {
        'product': product
    }
    return render(request, 'cart/cart_delete.html', context)
