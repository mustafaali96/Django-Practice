from django.contrib import admin
from custom_app.models import User, Courses
# Register your models here.
admin.site.register(User)  
admin.site.register(Courses)