from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Menu, Home, Reservation
from .forms import ReservationTableForm
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.forms import Form
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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
                message = form.cleaned_data['message']
                success_msg = self.validate_reservation(request.user, reservation_date, reservation_time)
                # error_msg = self.validate_reservation(request.user, reservation_date, reservation_time)
                if success_msg:
                    reservation = Reservation(user=request.user, reservation_date=reservation_date, reservation_time=reservation_time, message=message)
                    reservation.save()
                    user_reservations = Reservation.objects.filter(user=request.user)
                    return render(request, 'my_reservations.html', {'user_reservations': user_reservations})
                else:
                    return redirect('reservation.html', {'form': form})
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


class MyReservations(ListView):
    model = Reservation
    template_name = 'my_reservations.html'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class UpdateReservation(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationTableForm
    template_name = 'my_reservations.html'

    def get_success_url(self):
        return reverse_lazy('my_reservations')

