from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views.generic import (
  View,
  ListView,
  CreateView,
  UpdateView
)

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
class ProfileCreateView(CreateView):
  queryset = Profile.objects.all()
  template_name = 'profiles/profile_create.html'
  form_class = ProfileForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    messages.success(self.request, 'Profile created successfully!')
    return super(ProfileCreateView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(ProfileCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Profile Create'


# Profile Update View
class ProfileUpdateView(UpdateView):
  queryset = Profile.objects.all()
  template_name = 'profiles/profile_update.html'
  form_class = ProfileForm

  def get_object(self):
    id = self.kwargs.get('pk')
    return get_object_or_404(Profile, pk=id, user=self.request.user)
  
  def form_valid(self, form):
    messages.success(self.request, 'Profile updated successfully!')
    return super(ProfileUpdateView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(ProfileUpdateView, self).get_context_data(**kwargs)
    context['title'] = 'Profile Update'
    return context 


# Profile Create Experience View
class ExperienceCreateView(CreateView):
  queryset = Experience.objects.all()
  template_name = 'profiles/profile_create_experience.html'
  form_class = ExperienceForm

  def get_object(self):
    id = self.kwargs.get('pk')
    return get_object_or_404(Profile, pk=id, user=self.request.user)

  def form_valid(self, form):
    if self.get_object():
      form.instance.profile = self.get_object()
      return super(ExperienceCreateView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(ExperienceCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Experience Create'
    return context

  def get_success_url(self):
    messages.success(self.request, f'An experience cretated for {self.request.user}')
    return self.get_object().get_experience_url()


# Profile Experiences List View
class ExperienceListView(View):
  def get_object(self):
    return get_object_or_404(Profile, pk=self.kwargs.get('pk'))

  def get(self, request, pk=None, *args, **kwargs):
    if self.get_object():
      experiences = self.get_object().experience_set.all()
      if not experiences and self.get_object().user == request.user:
        return redirect(f'{self.get_object().get_experience_url()}create')
      context = {
        'title': 'Experiences',
        'experiences': experiences,
        'profile': self.get_object()
      }
    return render(request, 'profiles/profile_experience_list.html', context)


# Profile Experience Update View
class ExperienceUpdateView(UpdateView):
  queryset = Experience.objects.all()
  template_name = 'profiles/profile_experience_update.html'
  form_class = ExperienceForm
  profile = None

  def get_object(self):
    self.profile = get_object_or_404(Profile, user=self.request.user)
    if self.profile is not None:
      experience = get_object_or_404(
        Experience,
        pk=self.kwargs.get('pk'),
        profile=self.request.user.profile
      )
      return experience
    return profile
  
  def form_valid(self, form):
    return super(ExperienceUpdateView, self).form_valid(form)
  
  def get_context_data(self, **kwargs):
    context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
    context['title'] = 'Experience Update'
    return context
  
  def get_success_url(self):
    messages.success(self.request, 'An experience updated!')
    return self.profile.get_experience_url()



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
