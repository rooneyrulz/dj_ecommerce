from django.urls import path

from .views import users_signup_view

urlpatterns = [
    path('sign-up/', users_signup_view, name='users_sign_up_view')
]
