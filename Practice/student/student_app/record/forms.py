from django import forms
from .models import Record

class recordCreate(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'