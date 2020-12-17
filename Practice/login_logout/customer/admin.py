from django.contrib import admin
from .models import customer_model, customer_product_model
# Register your models here.

admin.site.register(customer_model) 
admin.site.register(customer_product_model)