from django.urls import path
from .views import (
    product_list_view,
    product_details_view,
    product_create_view,
    product_update_view,
    product_add_to_cart_view,
    product_delete_view,
    product_like_view,
    product_unlike_view
)

app_name = 'products'
urlpatterns = [
    path(
        '',
        product_list_view,
        name='product_list_view'
    ),
    path(
        'create/',
        product_create_view,
        name='product_create_view'
    ),
    path(
        '<int:pk>/details',
        product_details_view,
        name='product_details_view'
    ),
    path(
        '<int:pk>/edit',
        product_update_view,
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
        product_add_to_cart_view,
        name='product_add_to_cart_view'
    ),
    path(
        '<int:pk>/delete',
        product_delete_view,
        name='product_delete_view'
    )
]
