from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


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
      User,
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
        return reverse("profiles:profile_detail", kwargs={"pk": self.pk})


class Experience(models.Model):
    profile = models.OneToOneField(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )


class Education(models.Model):
    profile = models.OneToOneField(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )


class Social(models.Model):
    profile = models.OneToOneField(
      Profile,
      default=1,
      on_delete=models.CASCADE
    )
