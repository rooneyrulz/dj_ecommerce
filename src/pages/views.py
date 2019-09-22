from django.shortcuts import render

# Landing Page View
def landing_page_view(request):
  return render(request, 'pages/home.html', {})


# About Page View
def about_page_view(request):
  return render(request, 'pages/about.html', {})