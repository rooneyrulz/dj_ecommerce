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
      blank=True,
      null=True
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
    age = models.IntegerField(
      blank=True,
      null=True
    )
    status = models.CharField(
      max_length=50,
      choices=STATUS_CHOICES,
      default=1
    )
    skills = models.TextField(
      default='Marketing, Programming'
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

    def get_experience_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_create_experience",
          kwargs={"pk": self.pk})

    def get_education_url(self, *args, **kwargs):
        return reverse(
          "profiles:profile_create_education",
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
      blank=True,
      null=True
    )
    location = models.CharField(
      max_length=100,
      blank=True,
      null=True
    )
    worked_from = models.DateField(
      blank=True,
      null=True
    )
    worked_until = models.DateField(
      blank=True,
      null=True
    )
    currently_work_here = models.BooleanField(
      default=False
    )
    description = models.TextField(
      blank=True,
      null=True
    )
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self):
        return self.title


class Education(models.Model):
    profile = models.ForeignKey(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )
    school = models.CharField(
      max_length=120,
      blank=True,
      null=True
    )
    degree = models.CharField(
      max_length=100,
      blank=True,
      null=True
    )
    field_of_study = models.CharField(
      max_length=150,
      blank=True,
      null=True
    )
    studied_from = models.DateField(
      blank=True,
      null=True
    )
    studied_until = models.DateField(
      blank=True,
      null=True
    )
    currently_studying = models.BooleanField(
      default=False
    )
    description = models.TextField(
      blank=True,
      null=True
    )
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self):
        return self.school


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
