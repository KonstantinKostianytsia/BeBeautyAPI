from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthVariant(models.TextChoices):
        APPLE = 'APPLE'
        GOOGLE = 'GOOGLE'
        FACEBOOK = 'FACEBOOK'

class CustomUser(AbstractUser):
    auth_variant = models.CharField(
        max_length=8,
        choices=AuthVariant.choices
    )
