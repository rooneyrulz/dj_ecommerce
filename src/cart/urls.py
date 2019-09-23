from django.urls import path

from .views import cart_list_view

urlpatterns = [
    path(
        '',
        cart_list_view,
        name='cart_list_view'
    )
]
