# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from model_utils import Choices

class User(AbstractUser):
    subjects = Choices('Maths', 'Programming', 'Science', 'Electrical')
    subject = models.CharField(max_length=30, choices=subjects, 
                               default=subjects.Science, 
                               help_text = ('Enter your Subject'))
    roles = Choices('Student', 'Teacher')
    role = models.CharField(max_length=20, choices=roles,
                  default=roles.Student)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username