from django.shortcuts import render

from .models import Product
from .forms import ProductForm


# List out all products
def product_list_view(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request, 'products/product_list.html', context)


# Products details view
def product_details_view(request, pk):
	return render(request, 'products/product_details.html', {})


# Product create view
def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, 'products/product_create.html', context)


# Product update view
def product_update_view(request, pk):
	return render(request, 'products/product_update.html', {})


# Product add to cart view
def product_add_to_cart_view(request, pk):
	return render(request, 'products/product_add_to_cart.html', {})


# Product delete view
def product_delete_view(request, pk):
	return render(request, 'products/product_delete.html', {})