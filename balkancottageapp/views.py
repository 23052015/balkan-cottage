from django.shortcuts import render, redirect
from django.views import generic
from .models import Menu, Home, Reservation, Table
from .forms import ReservationTableForm
from django.contrib.auth.decorators import login_required
from django.forms import Form
from datetime import datetime, timedelta


class HomePage(generic.ListView):
    model = Home
    template_name = 'index.html'


class MenuList(generic.ListView):
    model = Menu
    # decide by which order to sort later
    queryset = Menu.objects.filter(status=1).order_by('-price')
    template_name = 'menu.html'
    paginate_by = 6


class Reservation(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'
    

@login_required()
def reserve_table(request):
    if request.method == 'Post':
        form = ReservationTableForm(request.Post)
        if form.is_valid:
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            table = form.cleaned_data['table']
            success_msg = validate_reservation(request.user, reservation_date, reservation_time, table)
            error_msg = validate_reservation(request.user, reservation_date, reservation_time, table)
            if success_msg:
                return "Congratulations, your booking is confirmed"
            else:
                return "Unfortunately the booking is not confirmed"
    else:
        form = ReservationTableForm()
    return render(request, 'reservation.html')
        

def validate_reservation(user, reservation_date, reservation_time):
    """
    This functions validates the reservation by checking the existence
    of another reservation indicating potential overlapping and avoiding
    conflicts if there is a reservation in a certain time period.
    """
    reservation_start_time = datetime.combine(reservation_date, reservation_time)
    reservation_end_time = reservation_start_time + timedelta(hours=2)
    existing_reservation = Reservation.objects.filter(
        reservation_date=reservation_date,
        table=table_number,
        reservation_time >= reservation_end_time,
        reservation_time <= reservation_start_time
    )
    if existing_reservation.exists():
        return False, "Ups, the table is already booked in the selected period"
    try:
        table_nr = Table.objects.get(table_number=table_number)
    except Table.DoesNotExist:
        return False, "Invalid table number selected."
    if not table_nr.is_available:
        return False, "Ups, the table is not available for reservation at the moment"
    if table_nr.capacity == '4' and existing_reservation.count() >=4:
        return False, "Sorry, the table is fully booked for the selected time"
    elif table_nr.capacity == '8' and existing_reservation.count() >=8:
        return False, "Sorry, the table is fully booked for the selected time"
    elif table_nr.capacity == '10' and existing_reservation.count() >=10:
        return False, "Sorry, the table is fully booked for the selected time"
    return True, None


def confirm_reservation(user, reservation_date, reservation_time, table_number):
    reservation = Reservation(user=user, table=table_number, reservation_date=reservation_date, reservation_time=reservation_time)
    reservation.save()
    table_nr = Table.objects.get(table_number=table_number)
    table_nr.is_available = False
    table_nr.save()
