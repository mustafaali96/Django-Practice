from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractUser):
    subject = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username