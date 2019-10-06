from django.contrib.auth.views import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product, Like
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
			try:
				cart_item = Cart.objects.get(product=pk, user=request.user)
				if cart_item:
					messages.error(request, 'Item is already in your cart!')
					return redirect('/products')
			except Cart.DoesNotExist:
				item = form.save(commit=False)
				item.product = product
				item.user = request.user
				form.save()
				messages.success(request, 'Item has been added to your cart!')
				return redirect('/products')
	
	context = {
		'form': form,
		'product': product
	}
	return render(request, 'products/product_add_to_cart.html', context)


# Product delete view
def product_delete_view(request, pk):
	return render(request, 'products/product_delete.html', {})


# Product Like View
@login_required()
def product_like_view(request, pk):
	product = get_object_or_404(Product, pk=pk)
	is_liked = Like.objects.filter(user=request.user, product=product)
	if is_liked:
		messages.error(request, 'Product has already been liked!')
		return redirect('/products')
	like = Like.objects.create(user=request.user, product=product)
	like.save()
	messages.success(request, 'Product has been liked!')
	return redirect('/products')


# Product Like View
@login_required()
def product_unlike_view(request, pk):
	product = get_object_or_404(Product, pk=pk)
	is_liked = Like.objects.filter(user=request.user, product=product)
	if is_liked:
		is_liked.delete()
		messages.success(request, 'Product has been unliked!')
		return redirect('/products')
	messages.error(request, 'Product has not been liked!')
	return redirect('/products')
	