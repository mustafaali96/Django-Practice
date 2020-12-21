from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserModel(User):

    subject = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    def __str__(self):
        return self.username