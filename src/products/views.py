from django.shortcuts import render

# List out all products
def product_list_view(request):
  return render(request, 'products/product_list.html', {})


# Products details view
def product_details_view(request, pk):
  return render(request, 'products/product_details.html', {})


# Product create view
def product_create_view(request):
  return render(request, 'products/product_create.html', {})


# Product update view
def product_update_view(request, pk):
  return render(request, 'products/product_update.html', {})


# Product add to cart view
def product_add_to_cart_view(request, pk):
  return render(request, 'products/product_add_to_cart.html', {})


# Product delete view
def product_delete_view(request, pk):
  return render(request, 'products/product_delete.html', {})