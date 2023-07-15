from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ('car', 'from_destination', 'to_destination', 'price', 'price_type', 'pick_up_date', 'pick_up_time', 'end_time')