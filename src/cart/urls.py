from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CartListView, CartDeleteView

app_name = 'cart'
urlpatterns = [
    path(
        '',
        login_required(CartListView.as_view()),
        name='cart_list_view'
    ),
    path(
        '<int:pk>/delete/',
        login_required(CartDeleteView.as_view()),
        name='cart_item_delete_view'
    )
]
