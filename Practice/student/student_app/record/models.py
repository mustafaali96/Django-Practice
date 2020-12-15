from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length = 30)
    student_email = models.EmailField(blank = False)
    student_number = models.TextField(default = "03XX-XXXXXXX")
    
    def __str__(self):
        return self.name
    