from django.shortcuts import render

from .models import Profile


# Profiles List View
def profile_list_view(request):
    profiles = Profile.objects.all()
    context = {
      'profiles': profiles
    }
    return render(request, 'profiles/profile_list.html', context)
