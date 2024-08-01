# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom User model with additional fields
    """
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True)
    address = models.TextField(_('address'), blank=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True)
    bio = models.TextField(_('bio'), blank=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    """
    Profile model with additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    interests = models.ManyToManyField('Interest', related_name='profiles', blank=True)
    skills = models.ManyToManyField('Skill', related_name='profiles', blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Interest(models.Model):
    """
    Interest model
    """
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    """
    Skill model
    """
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __str__(self):
        return self.name
