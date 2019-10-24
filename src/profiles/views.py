from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View, ListView

from .models import Profile, Experience, Education, Social
from .forms import (
  ProfileForm,
  ExperienceForm,
  EducationForm,
  SocialForm
)


# Profiles List View
class ProfileListView(ListView):
  queryset = Profile.objects.all()
  context_object_name = 'profiles'

  def get_context_data(self, **kwargs):
    context = super(ProfileListView, self).get_context_data(**kwargs)
    context['title'] = 'Profiles'
    return context


# Profile Detail View
class ProfileDetailView(View):
  template = 'profiles/profile_detail.html'
  context = {
    'title': 'Profile Details'
  }
  
  def get_object(self):
    id = self.kwargs.get('pk')
    return get_object_or_404(Profile, pk=id)

  def get(self, request, pk=None, *args, **kwargs):
    try:
      social = Social.objects.get(profile=self.get_object())
      form = SocialForm(instance=social)
      self.context['profile'] = self.get_object()
      self.context['form'] = form
    except Social.DoesNotExist:
      form = SocialForm()
      self.context['profile'] = self.get_object()
      self.context['form'] = form
    return render(request, self.template, self.context)

  def post(self, request, pk=None, *args, **kwargs):
    try:
      social = Social.objects.get(profile=self.get_object())
      form = SocialForm(request.POST, instance=social)
      self.context['profile'] = self.get_object()
      self.context['form'] = form
      if form.is_valid():
        form.save()
        messages.success(request, 'Social links updated successfully')
    except Social.DoesNotExist:
      form = SocialForm(request.POST)
      self.context['profile'] = self.get_object()
      self.context['form'] = form
      if form.is_valid():
        obj = form.save(commit=False)
        obj.profile = self.get_object()
        form.save()
        messages.success(request, 'Social links added successfully')
    return render(request, self.template, self.context)




# Profile Create View
@login_required()
def profile_create_view(request):
    # if request.user.profile:
    #     return redirect(request.user.profile.get_absolute_url())
    form = ProfileForm(
      request.POST or None,
      request.FILES or None
    )
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        messages.success(request, 'Profile created successfully!')
        return redirect(request.user.profile.get_absolute_url())
    context = {
      'title': 'Create Profile',
      'form': form
    }
    return render(request, 'profiles/profile_create.html', context)


# Profile Create View
@login_required()
def profile_update_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
    form = ProfileForm(
      request.POST or None,
      request.FILES or None,
      instance=request.user.profile
    )
    if form.is_valid():
        profile = form.save(commit=False)
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
    profile = get_object_or_404(Profile, pk=pk, user=request.user)
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
    if not experiences and profile.user == request.user:
        return redirect(f'{profile.get_experience_url()}create')
    context = {
      'title': 'Experiences',
      'experiences': experiences,
      'profile': profile
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
    profile = get_object_or_404(Profile, pk=pk)
    educations = profile.education_set.all()
    if not educations and profile.user == request.user:
        return redirect(f'{profile.get_education_url()}create')
    context = {
      'title': 'Educations',
      'educations': educations,
      'profile': profile
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
@login_required()
def profile_education_update_view(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    education = get_object_or_404(
      Education,
      pk=pk,
      profile=request.user.profile
    )
    form = EducationForm(request.POST or None, instance=education)
    if form.is_valid():
        form.save()
        messages.success(request, 'An education updated!')
        return redirect(profile.get_education_url())
    context = {
      'title': 'Educations',
      'form': form,
      'edu': education,
      'profile': profile
    }
    return render(request, 'profiles/profile_education_update.html', context)


# Profile Education Delete View
@login_required()
def profile_education_delete_view(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    education = get_object_or_404(
      Education,
      pk=pk,
      profile=request.user.profile
    )
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'An education deleted!')
        return redirect(profile.get_education_url())
    context = {
      'title': 'Delete Education',
      'profile': profile,
      'edu': education
    }
    return render(request, 'profiles/profile_education_delete.html', context)
