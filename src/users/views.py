from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserSignUpForm


# Users Signup View
def users_signup_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    form = UserSignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "You are registered! Let's login!")
        return redirect('/users/sign-in')
    context = {
        'title': 'Sign-Up',
        'form': form
    }
    return render(request, 'users/users_signup.html', context)


# Delete Account View
def users_account_delete_view(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if user:
        user.delete()
        messages.success(request, 'Your account destroyed!')
        return redirect('/')
    messages.error(request, 'Oops! Something went wrong!')
    return redirect('/dashboard')
