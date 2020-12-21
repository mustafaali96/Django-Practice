from django.db import models

from django.contrib.auth.models import AbstractUser

class regUser(AbstractUser):

    subject = models.CharField(max_length=30)
    role = models.CharField(max_length=30)