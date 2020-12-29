from django import forms
from django.forms import PasswordInput, TextInput
from custom_app.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password","subject", "role", )
        widgets = {
        'password': forms.PasswordInput(attrs={'placeholder': 'password', 'autocomplete': 'off'}),
        'username': forms.TextInput(attrs={'placeholder': 'username', 'autocomplete': 'off'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'first name', 'autocomplete': 'off'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'last name', 'autocomplete': 'off'}),
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

class updateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username","subject", "role", "user_image")
        widgets = {
        'password': forms.PasswordInput(attrs={'placeholder': 'new password'}),
        'username': forms.TextInput(attrs={'placeholder': 'new username'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
        'user_image': forms.FileInput(attrs={'class': 'form-control-user', 'accept': 'image/*'}), 
        }
