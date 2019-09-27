from django.urls import path

from .views import profile_list_view

urlpatterns = [
    path('', profile_list_view, name='profile_list_view')
]
