from django import forms
from .models import Profile, Education, Experience, Social


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter your name'
        }
      )
    )
    profession = forms.Select()
    company = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter company'
        }
      )
    )
    website = forms.CharField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Enter your website'
        }
      )
    )
    location = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter location'
        }
      )
    )
    gender = forms.Select()
    age = forms.IntegerField(
      widget=forms.NumberInput(
        attrs={
          'placeholder': 'Enter your age'
        }
      )
    )
    status = forms.Select()
    skills = forms.CharField(
      required=False,
      widget=forms.Textarea(
        attrs={
          'placeholder': 'Leave some of your skills',
          'rows': 4
        }
      )
    )
    bio = forms.CharField(
      required=False,
      widget=forms.Textarea(
        attrs={
          'placeholder': 'About you',
          'rows': 4
        }
      )
    )
    image = forms.ImageField(
      required=False
    )

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

    def clean_age(self, *args, **kwargs):
        age = self.cleaned_data.get('age')
        if not (age > 17 and age < 50):
            raise forms.ValidationError('Age must be between 17-50')
        else:
            return age


# Model Form - Experience
class ExperienceForm(forms.ModelForm):
    title = forms.Select()
    company = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter company'
        }
      )
    )
    location = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter location'
        }
      )
    )
    worked_from = forms.DateField(
      widget=forms.SelectDateWidget()
    )
    worked_until = forms.DateField(
      widget=forms.SelectDateWidget()
    )
    currently_work_here = forms.CheckboxInput()
    description = forms.CharField(
      required=False,
      widget=forms.Textarea(
        attrs={
          'placeholder': 'Leave some message about your experience',
          'rows': 4
        }
      )
    )

    class Meta:
        model = Experience
        fields = [
          'title',
          'company',
          'location',
          'worked_from',
          'worked_until',
          'currently_work_here',
          'description'
        ]

    def clean_company(self, *args, **kwargs):
        company = self.cleaned_data.get('company')
        if not company.strip():
            raise forms.ValidationError('Please enter a valid company name!')
        else:
            return company


# Model Form - Education
class EducationForm(forms.ModelForm):
    school = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter your school'
        }
      )
    )
    degree = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter your school'
        }
      )
    )
    field_of_study = forms.CharField(
      widget=forms.TextInput(
        attrs={
          'placeholder': 'Enter your school'
        }
      )
    )
    studied_from = forms.DateField(
      widget=forms.SelectDateWidget()
    )
    studied_until = forms.DateField(
      widget=forms.SelectDateWidget()
    )
    currently_studying = forms.CheckboxInput()
    description = forms.CharField(
      required=False,
      widget=forms.Textarea(
        attrs={
          'placeholder': 'Enter your school',
          'rows': 4
        }
      )
    )

    class Meta:
        model = Education
        fields = [
          'school',
          'degree',
          'field_of_study',
          'studied_from',
          'studied_until',
          'currently_studying',
          'description'
        ]


# Model Form - Social
class SocialForm(forms.ModelForm):
    youtube = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Youtube link'
        }
      )
    )
    twitter = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Twitter link'
        }
      )
    )
    facebook = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Facebook link'
        }
      )
    )
    linkedin = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Linkedin link'
        }
      )
    )
    instagram = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Instagram link'
        }
      )
    )
    github = forms.URLField(
      required=False,
      widget=forms.URLInput(
        attrs={
          'placeholder': 'Github link'
        }
      )
    )

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
