from django import forms
from django.forms import PasswordInput, TextInput
from custom_app.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password","subject", "role", )
        widgets = {
        'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        'username': forms.TextInput(attrs={'placeholder': 'username'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
        }
        help_texts = {
            'password': ('Use Strong Password.'),
        }
        error_messages = {
            'username': {
                'max_length': ("This username is already taken."),
            },
        }
        # username = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'autocomplete': 'off'}))
        
    def save(self):
        return User.objects.create_user(**self.cleaned_data)

class updateCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username","subject", "role", )