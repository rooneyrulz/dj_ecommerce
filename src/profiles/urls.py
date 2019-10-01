from django.urls import path

from .views import profile_list_view, profile_detail_view

app_name = 'profiles'
urlpatterns = [
    path(
        '',
        profile_list_view,
        name='profile_list'
    ),
    path(
        '<int:pk>/detail/',
        profile_detail_view,
        name='profile_detail'
    )
]
