from django.shortcuts import render, redirect
from django.views.generic import View


# Landing Page View
class LandingView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashboard')
        return render(request, 'pages/home.html', {})


# About Page View
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/about.html', {})


# Dashboard Page View
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'pages/dashboard.html', {})
        return redirect('/')
        