from django.shortcuts import render, redirect


# Landing Page View
def landing_page_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard') 
    return render(request, 'pages/home.html', {})


# About Page View
def about_page_view(request):
    return render(request, 'pages/about.html', {})


# Dashboard Page View
def dashboard_page_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'pages/dashboard.html', {})
        