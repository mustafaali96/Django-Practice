from django.db import models

# Create your models here.
class customer_model(models.Model):
    cust_id = models.CharField(max_length = 40)
    cust_name = models.CharField(max_length = 30)
    cust_details = models.TextField(max_length = 40)
    def __str__(self):
        return self.cust_id

class customer_product_model(models.Model):
    product_name = models.CharField(max_length = 50)
    product_quantity = models.IntegerField()
    purchased_by = models.ForeignKey(customer_model, on_delete = models.CASCADE)

    def __str__(self):
        return self.product_name