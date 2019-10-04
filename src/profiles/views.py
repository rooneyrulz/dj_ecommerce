from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile, Experience, Education, Social
from .forms import (
  ProfileForm,
  ExperienceForm,
  EducationForm,
  SocialForm
)


# Profiles List View
def profile_list_view(request):
    profiles = Profile.objects.all()
    context = {
      'profiles': profiles
    }
    return render(request, 'profiles/profile_list.html', context)


# Profile Detail View
def profile_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    try:
        social = Social.objects.get(profile=profile)
        form = SocialForm(request.POST or None, instance=social)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social links updated successfully')
        context = {
          'profile': profile,
          'form': form
        }
    except Social.DoesNotExist:
        form = SocialForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = profile
            form.save()
            messages.success(request, 'Social links added successfully')
        context = {
          'profile': profile,
          'form': form
        }
    return render(request, 'profiles/profile_detail.html', context)


# Profile Create View
@login_required()
def profile_create_view(request):
    form = ProfileForm(
      request.POST or None,
      request.FILES or None
    )
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
    context = {
      'title': 'Create Profile',
      'form': form
    }
    return render(request, 'profiles/profile_create.html', context)


# Profile Create View
@login_required()
def profile_update_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(
      request.POST or None,
      request.FILES or None,
      instance=profile
    )
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect(profile.get_absolute_url())
    context = {
      'title': 'Update Profile',
      'form': form,
      'profile': profile
    }
    return render(request, 'profiles/profile_update.html', context)


# Profile Create Experience View
def profile_create_experience_view(request, pk):
    form = ExperienceForm(request.POST or None)
    context = {
      'title': 'Experiences',
      'form': form
    }
    return render(request, 'profiles/profile_create_experience.html', context)


# Profile Create Education View
def profile_create_education_view(request, pk):
    form = EducationForm(request.POST or None)
    context = {
      'title': 'Educations',
      'form': form
    }
    return render(request, 'profiles/profile_create_education.html', context)
