from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserSignUpForm


# Users Signup View
class SignupView(CreateView):
    queryset = User.objects.all()
    template_name = 'users/users_signup.html'
    success_url = '/users/sign-in'
    form_class = UserSignUpForm

    def form_valid(self, form):
        obj = super(SignupView, self).form_valid(form)
        messages.success(self.request, "You are registered! Let's login!")
        return obj

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['title'] = 'Sign-Up'
        return context


# Delete Account View
class AccountDeleteView(View):
    def get_object(self):
        user = get_object_or_404(User, pk=self.request.user.pk)
        if user is not None:
            return user
        return None

    def post(self, request, pk=None, *args, **kwargs):
        user = self.get_object()
        if user is not None:
            user.delete()
            messages.success(request, 'Your account destroyed!')
            return redirect('/')
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('/dashboard')
