from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
      User,
      default=1,
      on_delete=models.CASCADE
    )
    name = models.CharField(
      max_length=120,
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
      max_length=50,
      default='Male'
    )
    age = models.IntegerField(
      blank=True,
      null=True
    )
    status = models.CharField(
      max_length=50,
      default='Married'
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
      auto_now_add=True,
    )


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
