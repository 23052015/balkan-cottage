from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Menu, Home
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
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
