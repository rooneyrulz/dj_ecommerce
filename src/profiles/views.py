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
@login_required()
def profile_create_experience_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = ExperienceForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.profile = profile
        form.save()
        messages.success(request, f'An experience cretated for {request.user}')
        return redirect(profile.get_experience_url())
    context = {
      'title': 'Experiences',
      'form': form
    }
    return render(request, 'profiles/profile_create_experience.html', context)


# Profile Experiences List View
@login_required()
def profile_experience_list_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    experiences = profile.experience_set.all()
    context = {
      'title': 'Experiences',
      'experiences': experiences
    }
    return render(request, 'profiles/profile_experience_list.html', context)


# Profile Experience Update View
@login_required()
def profile_experience_update_view(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    experience = get_object_or_404(
      Experience,
      pk=pk,
      profile=request.user.profile
    )
    form = ExperienceForm(
      request.POST or None,
      instance=experience
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'An experience updated!')
        return redirect(profile.get_experience_url())
    context = {
      'title': 'Update Experience',
      'form': form
    }
    return render(request, 'profiles/profile_experience_update.html', context)


# Profile Experience Delete View
@login_required()
def profile_experience_delete_view(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'An experience deleted!')
        return redirect(profile.get_experience_url())
    context = {
      'title': 'Experience Delete',
      'profile': profile,
      'exp': experience
    }
    return render(request, 'profiles/profile_experience_delete.html', context)


# Profile Education List View
@login_required()
def profile_education_list_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    educations = profile.education_set.all()
    context = {
      'title': 'Educations',
      'educations': educations
    }
    return render(request, 'profiles/profile_education_list.html', context)


# Profile Create Education View
@login_required()
def profile_create_education_view(request, pk):
    profile = get_object_or_404(
      Profile,
      pk=pk,
      user=request.user
    )
    form = EducationForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.profile = profile
        form.save()
        messages.success(request, f'An education created for {request.user}')
        return redirect(profile.get_education_url())
    context = {
      'title': 'Educations',
      'form': form
    }
    return render(request, 'profiles/profile_create_education.html', context)


# Profile Education Update View
def profile_education_update_view(request, pk):
    context = {}
    return render(request, 'profiles/profile_education_update.html', context)


# Profile Education Delete View
def profile_education_delete_view(request, pk):
    context = {}
    return render(request, 'profiles/profile_education_delete.html', context)
