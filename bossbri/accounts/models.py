# models.py

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Custom User Model
class User(AbstractUser, PermissionsMixin):
    """
    Custom User Model with additional fields
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        ),
    ])
    address = models.TextField(_('address'), blank=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True)
    bio = models.TextField(_('bio'), blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

# Profile Model
class Profile(models.Model):
    """
    Profile Model with additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    following = models.ManyToManyField(User, related_name='followers', blank=True)
    interests = ArrayField(models.CharField(max_length=50), blank=True)
    skills = ArrayField(models.CharField(max_length=50), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal to create a Profile instance when a User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Custom Manager for User model
class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_admin=False)

User.objects = UserManager()
User.active = ActiveUserManager()
