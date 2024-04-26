from django import forms
from .models import booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['host_name', 'class_name', 'students', 'subject', 'timing']