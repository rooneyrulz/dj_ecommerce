from django.urls import path

from .views import landing_page_view, about_page_view, dashboard_page_view

urlpatterns = [
  path('', landing_page_view, name='landing_page_view'),
  path('dashboard/', dashboard_page_view, name='dashboard_page_view'),
  path('about/', about_page_view, name='about_page_view')
]