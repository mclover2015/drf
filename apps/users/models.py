from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.enum_regex import Regex
from core.models import BaseModel
from core.services.upload_avatar import upload_avatar

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.NAME.value)])
    surname = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.NAME.value)])
    age = models.IntegerField(validators=[V.MinValueValidator(18), V.MaxValueValidator(100)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, upload_to=upload_avatar)
