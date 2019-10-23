from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.generic import (
	View,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from django.contrib import messages
from django.http import Http404

from .models import Product, Like
from cart.models import Cart

from .forms import ProductForm
from cart.forms import CartForm


# List out all products
class ProductListView(ListView):
	queryset = Product.objects.all()
	context_object_name = 'products'

	def get_context_data(self, **kwargs):
		context = super(ProductListView, self).get_context_data(**kwargs)
		context['title'] = 'Products'
		return context


# Products details view
class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	context_object_name = 'product'

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['title'] = 'Product Details'
		return context


# Product create view
class ProductCreateView(CreateView):
	queryset = Product.objects.all()
	template_name = 'products/product_create.html'
	form_class = ProductForm

	def form_valid(self, form):
		return super(ProductCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ProductCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Product Create'
		return context


# Product update view
class ProductUpdateView(UpdateView):
	queryset = Product.objects.all()
	template_name = 'products/product_update.html'
	form_class = ProductForm

	def form_valid(self, form):
		messages.success(self.request, 'Product has been updated successfully!')
		print(form.cleaned_data)
		return super(ProductUpdateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ProductUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Product Update'
		return context


# Product Add To Cart View
class AddToCartView(View):
	def get_object(self):
		product_id = self.kwargs.get('pk')
		return get_object_or_404(Product, pk=product_id)

	def get(self, request, pk=None, *args, **kwargs):
		form = CartForm()
		context = {
			'form': form,
			'product': self.get_object()
		}
		return render(request, 'products/product_add_to_cart.html', context)

	def post(self, request, pk=None, *args,**kwargs):
		form = CartForm(request.POST)
		if form.is_valid():
			try:
				item = Cart.objects.get_cart_item(self.get_object(), request.user)
				if item:
					messages.error(request, 'Item is already in your cart!')
					return redirect('/products')
			except Cart.DoesNotExist:
				item = form.save(commit=False)
				item.product = self.get_object()
				item.user = request.user
				form.save()
				messages.success(request, 'Item has been added to your cart!')
				return redirect('/products')


# Product delete view
class ProductDeleteView(DeleteView):
	queryset = Product.objects.all()
	template_name = 'products/product_delete.html'
	context_object_name = 'product'
	success_url = '/products'

	def get_context_data(self, **kwargs):
		context = super(ProductDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Product Delete'
		return context


# Product Like View
class ProductLikeView(View):
	def get_object(self):
		id = self.kwargs.get('pk')
		return get_object_or_404(Product, pk=id)
	
	def get(self, request, pk=None, *args, **kwargs):
		is_liked = Like.objects.get_like(request.user, self.get_object())
		if is_liked:
			messages.error(request, 'Product has already been liked!')
			return redirect('/products')
		like = Like.objects.create_like(request.user, self.get_object())
		messages.success(request, 'Product has been liked!')
		return redirect('/products')


# Product Like View
class ProductUnLikeView(View):
	def get_object(self):
		id = self.kwargs.get('pk')
		return get_object_or_404(Product, pk=id)
	
	def get(self, request, pk=None, *args, **kwargs):
		is_liked = Like.objects.get_like(request.user, self.get_object())
		if is_liked:
			is_liked.delete()
			messages.success(request, 'Product has been unliked!')
			return redirect('/products')
		messages.error(request, 'Product has not been liked!')
		return redirect('/products')
	