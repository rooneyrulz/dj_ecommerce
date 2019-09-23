from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# from .forms import UserForm


def users_signup_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/users_signup.html', context)
