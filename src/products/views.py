from django.contrib.auth.views import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product
from cart.models import Cart

from .forms import ProductForm, CartForm


# List out all products
def product_list_view(request):
	products = Product.objects.all()
	context = {
		'title': 'Products',
		'products': products
	}
	return render(request, 'products/product_list.html', context)


# Products details view
def product_details_view(request, pk):
	product = get_object_or_404(Product, id=pk)
	context = {
		'title': 'Product Details',
		'product': product
	}
	return render(request, 'products/product_details.html', context)


# Product create view
def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'title': 'Product Create',
		'form': form
	}
	return render(request, 'products/product_create.html', context)


# Product update view
def product_update_view(request, pk):
	return render(request, 'products/product_update.html', {})


# Product add to cart view
@login_required()
def product_add_to_cart_view(request, pk):
	product = get_object_or_404(Product, id=pk)
	form = CartForm(request.POST or None)
	if form.is_valid():
		item = form.save(commit=False)
		item.product = product
		item.user = request.user
		form.save()
		messages.success(request, 'Item has been added to your cart!')
	context = {
		'form': form,
		'product': product
	}
	return render(request, 'products/product_add_to_cart.html', context)


# Product delete view
def product_delete_view(request, pk):
	return render(request, 'products/product_delete.html', {})