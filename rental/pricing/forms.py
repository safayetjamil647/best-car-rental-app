from django import forms
from .models import Pricing

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'
