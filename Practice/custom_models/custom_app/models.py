# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from model_utils import Choices
from django.urls import reverse_lazy

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ManyToManyField('Courses') 
    roles = Choices('Student', 'Teacher')
    role = models.CharField(max_length=50, choices=roles) 
    user_image = models.ImageField(upload_to ='static/user_imgs/',
                                    null=True)

    def __str__(self):
        return self.username

    def detail_dis(self):
        return reverse_lazy('student_id_rec', kwargs={'user_id':self.pk})

class Courses(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    domain = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

