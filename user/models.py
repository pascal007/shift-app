from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.text import gettext_lazy as _

from core.models import BaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, is_admin=False):
        if not username:
            raise ValueError(_('Users must have a username'))

        user = self.model(
            username=username,
        )
        user.set_password(password)
        if is_admin:
            user.is_superuser = True
            user.is_staff = True
            user.role = 'ADMIN'
        user.save()
        return user

    def create_superuser(self, username, password):
        return self.create_user(username, password, is_admin=True)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(unique=True, max_length=15)
    role = models.CharField(max_length=10, default='WORKER')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

