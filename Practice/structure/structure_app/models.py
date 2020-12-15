from django.db import models

# Create your models here.
class new_structure(models.Model):
    name = models.CharField(max_length = 100)
    des = models.TextField(max_length = 50)
    def __str__(self):
        return self.name