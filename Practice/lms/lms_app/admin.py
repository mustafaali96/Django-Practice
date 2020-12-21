from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from lms_app.models import regUser
# Register your models here.
admin.site.register(regUser)