from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignupView, AccountDeleteView

urlpatterns = [
    path(
        'sign-up/',
        SignupView.as_view(),
        name='users_sign_up_view'
    ),
    path(
        'sign-in/',
        LoginView.as_view(template_name='users/users_login.html'),
        name='users_login_view'
    ),
    path(
        'sign-out/',
        LogoutView.as_view(template_name='users/users_logout.html'),
        name='users_logout_view'
    ),
    path(
        'destroy/',
        AccountDeleteView.as_view(),
        name='users_account_delete_view'
    )
]
