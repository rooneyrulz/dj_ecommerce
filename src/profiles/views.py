from django.shortcuts import render, get_object_or_404

from .models import Profile


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
    context = {
      'profile': profile
    }
    return render(request, 'profiles/profile_detail.html', context)
