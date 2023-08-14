from django import forms
from .models import Reservation
from datetime import datetime, timedelta



class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'message']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'})
        }
        message = forms.TextInput()