from django.urls import path

from .views import LandingView, AboutView, DashboardView

urlpatterns = [
  path(
    '',
    LandingView.as_view(),
    name='landing_page_view'
  ),
  path(
    'dashboard/',
    DashboardView.as_view(),
    name='dashboard_page_view'
  ),
  path(
    'about/',
    AboutView.as_view(),
    name='about_page_view'
  )
]