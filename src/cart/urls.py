from django.urls import path
from .views import cart_list_view, cart_item_delete_view

urlpatterns = [
    path(
        '',
        cart_list_view,
        name='cart_list_view'
    ),
    path(
        '<int:pk>/delete/',
        cart_item_delete_view,
        name='cart_item_delete_view'
    )
]
