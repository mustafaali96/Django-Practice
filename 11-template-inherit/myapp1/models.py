from django.db import models

# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
