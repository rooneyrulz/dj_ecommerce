from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    AddToCartView,
    product_delete_view,
    product_like_view,
    product_unlike_view
)

app_name = 'products'
urlpatterns = [
    path(
        '',
        ProductListView.as_view(),
        name='product_list_view'
    ),
    path(
        'create/',
        ProductCreateView.as_view(),
        name='product_create_view'
    ),
    path(
        '<int:pk>/details',
        ProductDetailView.as_view(),
        name='product_details_view'
    ),
    path(
        '<int:pk>/update',
        ProductUpdateView.as_view(),
        name='product_update_view'
    ),
    path(
        '<int:pk>/like',
        product_like_view,
        name='product_like_view'
    ),
    path(
        '<int:pk>/unlike',
        product_unlike_view,
        name='product_unlike_view'
    ),
    path(
        '<int:pk>/cart/add',
        login_required(AddToCartView.as_view()),
        name='product_add_to_cart_view'
    ),
    path(
        '<int:pk>/delete',
        product_delete_view,
        name='product_delete_view'
    )
]
