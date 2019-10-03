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


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = [
          'youtube',
          'twitter',
          'facebook',
          'linkedin',
          'instagram',
          'github'
        ]
