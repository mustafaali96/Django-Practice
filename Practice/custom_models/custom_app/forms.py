from django import forms
from django.forms import PasswordInput
from custom_app.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields = ("username", "password","subject", "role", )
    def save(self):
        return User.objects.create_user(**self.cleaned_data)

class recordCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","subject", "role", )