from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=40, unique=True)
    phone_number = models.IntegerField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        ordering = ['-date_joined']
    