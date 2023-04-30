from django import forms
from .models import Reservation, Table
from datetime import datetime, timedelta


class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'reservation_date', 'reservation_time']

