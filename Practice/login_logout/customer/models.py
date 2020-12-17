from django.db import models

# Create your models here.
class customer_model(models.Model):
    cust_name = models.CharField(max_length = 30)
    cust_details = models.TextField(max_length = 40)
    def __str__(self):
        return self.cust_name