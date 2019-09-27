from django.shortcuts import render


# Profiles List View
def profile_list_view(request):
    return render(request, 'profiles/profile_list.html', {})
