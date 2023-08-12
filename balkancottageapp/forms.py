from django import forms
from .models import Reservation
from datetime import datetime, timedelta


class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time']

