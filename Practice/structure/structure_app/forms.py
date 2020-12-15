from django import forms
from .models import new_structure

class new_structure_form(forms.ModelForm):
    class Meta:
        model = new_structure
        field = "__all__"