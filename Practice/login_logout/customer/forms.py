from django import forms
from .models import customer_model

class customer_form(forms.ModelForm):
    class Meta:
        model = customer_model
        fields = "__all__"

