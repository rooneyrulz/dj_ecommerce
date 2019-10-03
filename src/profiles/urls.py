from django.urls import path

from .views import (
    profile_list_view,
    profile_detail_view,
    profile_create_view,
    profile_update_view,
    profile_create_experience_view,
    profile_create_education_view
)

app_name = 'profiles'
urlpatterns = [
    path(
        '',
        profile_list_view,
        name='profile_list'
    ),
    path(
        'create/',
        profile_create_view,
        name='profile_create'
    ),
    path(
        '<int:pk>/detail/',
        profile_detail_view,
        name='profile_detail'
    ),
    path(
        '<int:pk>/update/',
        profile_update_view,
        name='profile_update'
    ),
    path(
        '<int:pk>/experience/create',
        profile_create_experience_view,
        name='profile_create_experience'
    ),
    path(
        '<int:pk>/education/create',
        profile_create_education_view,
        name='profile_create_education'
    )
]
