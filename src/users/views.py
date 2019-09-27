from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserSignUpForm


def users_signup_view(request):
    form = UserSignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserSignUpForm()
    context = {
        'title': 'Sign-Up',
        'form': form
    }
    return render(request, 'users/users_signup.html', context)
