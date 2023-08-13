from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Menu, Home, Reservation
from .forms import ReservationTableForm
from django.contrib.auth.decorators import login_required
from django.forms import Form
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(generic.ListView):
    model = Home
    template_name = 'index.html'


class MenuList(generic.ListView):
    model = Menu
    # decide by which order to sort later
    queryset = Menu.objects.filter(status=1).order_by('-price')
    template_name = 'menu.html'
    paginate_by = 6


class CreateReservation(LoginRequiredMixin, View):
    model = Reservation
    template_name = 'reservation.html'

    def get(self, request):
        form = ReservationTableForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = ReservationTableForm(request.POST)
            if form.is_valid():
                reservation_date = form.cleaned_data['reservation_date']
                reservation_time = form.cleaned_data['reservation_time']
                success_msg = self.validate_reservation(request.user, reservation_date, reservation_time)
                error_msg = self.validate_reservation(request.user, reservation_date, reservation_time)
                if success_msg:
                    reservation = Reservation(user=request.user, reservation_date=reservation_date, reservation_time=reservation_time)
                    reservation.save()
                    user_reservations = Reservation.objects.filter(user=request.user)
                    return redirect('my_reservations.html', {'user_reservations': user_reservations})
                else:
                    return render(request, 'reservation.html', {'form': form, 'error_msg': error_msg})
        else:
            form = ReservationTableForm()
        return render(request, 'reservation.html', {'form': form})
            
    def validate_reservation(self, user, reservation_date, reservation_time):
        """
        This functions validates the reservation by checking the existence
        of another reservation indicating potential overlapping and avoiding
        conflicts if there is a reservation in a certain time period.
        """
        reservation_start_time = datetime.combine(reservation_date, reservation_time)
        reservation_end_time = reservation_start_time + timedelta(hours=3)
        existing_reservation = Reservation.objects.filter(
            reservation_date=reservation_date,
            reservation_time__lte=reservation_end_time,
            reservation_time__gte=reservation_start_time
        )
        if existing_reservation.exists():
            return False, "Ups, there is already a reservation in the selected period"
        else:
            return True, None

