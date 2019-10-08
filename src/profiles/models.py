from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from datetime import datetime


GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]

STATUS_CHOICES = [
  ('Married', 'Married'),
  ('Single', 'Single')
]

PROFESSION_CHOICES = [
  ('Student or Learning', 'Student or Learning'),
  ('Junior Developer', 'Junior Developer'),
  ('Senior Developer', 'Senior Developer'),
  ('Developer', 'Developer'),
  ('Manager', 'Manager'),
  ('Instructor or Teacher', 'Instructor or Teacher'),
  ('Intern', 'Intern'),
  ('Bussiness Man', 'Bussiness Man'),
  ('Digital Marketer', 'Digital Marketer'),
  ('Data Scientist', 'Data Scientist'),
  ('Other', 'Other')
]


class Profile(models.Model):
    user = models.OneToOneField(
      settings.AUTH_USER_MODEL,
      default=1,
      on_delete=models.CASCADE
    )
    name = models.CharField(
      max_length=120,
    )
    profession = models.CharField(
      max_length=200,
      choices=PROFESSION_CHOICES,
      default=1
    )
    company = models.CharField(
      max_length=150,
      default='Some Company Pvt Ltd'
    )
    website = models.URLField(
      unique=True,
      blank=True,
      null=True
    )
    location = models.CharField(
      max_length=100,
      default='USA'
    )
    gender = models.CharField(
      max_length=6,
      choices=GENDER_CHOICES,
      default=1
    )
    age = models.IntegerField()
    status = models.CharField(
      max_length=50,
      choices=STATUS_CHOICES,
      default=1
    )
    skills = models.TextField(
      default='Marketing Programming',
      blank=True,
      null=True
    )
    bio = models.TextField(
      blank=True,
      null=True
    )
    image = models.ImageField(
      upload_to='profile_images/',
      default='default.jpg'
    )
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self, *args, **kwargs):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_detail",
          kwargs={"pk": self.pk}
        )

    def get_update_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_update",
          kwargs={"pk": self.pk}
        )

    def get_delete_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_delete",
          kwargs={"pk": self.pk}
        )

    def get_experience_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_experience_list",
          kwargs={"pk": self.pk}
        )

    def get_education_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_education_list",
          kwargs={"pk": self.pk}
        )


class Experience(models.Model):
    profile = models.ForeignKey(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )
    title = models.CharField(
      max_length=150,
      choices=PROFESSION_CHOICES,
      default=1
    )
    company = models.CharField(
      max_length=120,
      default='New Company Pvt Ltd'
    )
    location = models.CharField(
      max_length=100,
      default='Sri Lanka'
    )
    worked_from = models.DateField()
    worked_until = models.DateField()
    currently_work_here = models.BooleanField()
    description = models.TextField(
      blank=True,
      null=True
    )
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self):
        return self.title

    def get_update_url(self, *args, **kwargs):
        return reverse(
          'profiles:profile_experience_update',
          kwargs={'pk': self.pk}
        )

    def get_delete_url(self, *args, **kwargs):
        return reverse(
          'profiles:profile_experience_delete',
          kwargs={'pk': self.pk}
        )


class Education(models.Model):
    profile = models.ForeignKey(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )
    school = models.CharField(
      max_length=120,
      default='New Collage'
    )
    degree = models.CharField(
      max_length=100,
      default='BSC'
      )
    field_of_study = models.CharField(
      max_length=150,
      default='Computer Science'
      )
    studied_from = models.DateField()
    studied_until = models.DateField()
    currently_studying = models.BooleanField()
    description = models.TextField(
      blank=True,
      null=True
    )
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self):
        return self.school

    def get_update_url(self, *args, **kwargs):
        return reverse(
          'profiles:profile_education_update',
          kwargs={'pk': self.pk}
        )

    def get_delete_url(self, *args, **kwargs):
        return reverse(
          'profiles:profile_education_delete',
          kwargs={'pk': self.pk})


class Social(models.Model):
    profile = models.OneToOneField(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
