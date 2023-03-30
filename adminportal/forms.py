from django import forms
from app.models import Product

class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"


        