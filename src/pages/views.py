from django.http import HttpResponse
from django.shortcuts import render


# Landing Page View
def landing_page_view(request):
  return HttpResponse('<h1>Landing Page</h1>')


# About Page View
def about_page_view(request):
  return HttpResponse('<h1>About Page</h1>')
