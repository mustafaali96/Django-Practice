from django import forms
from lms_app.models import regUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # name = forms.CharField(required = True)
    # subject = forms.CharField(required = True)
    # role = forms.CharField(required = True)

    class Meta:
            model = regUser
            fields = ("username", "password1", "password2","subject", "role", )