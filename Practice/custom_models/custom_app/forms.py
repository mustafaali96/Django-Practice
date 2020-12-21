from django import forms
from custom_app.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password1': forms.PasswordInput(),
        'password2': forms.PasswordInput(),
    }
        fields = ("username", "password1", "password2","subject", "role", )