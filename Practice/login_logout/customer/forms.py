from django import forms
from .models import customer_model

class customer_form(forms.ModelForm):
    cust_details = forms.CharField(required=False)
    class Meta:
        model = customer_model
        # fields = "__all__"
        fields = ("cust_id","cust_name","cust_details",)

