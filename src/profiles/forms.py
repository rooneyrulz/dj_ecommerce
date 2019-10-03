from django import forms

from .models import Profile, Education, Experience, Social


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
          'name',
          'profession',
          'company',
          'website',
          'location',
          'gender',
          'age',
          'status',
          'skills',
          'bio',
          'image'
        ]
