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