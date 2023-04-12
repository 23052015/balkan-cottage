from django.shortcuts import render, redirect
from django.views import generic
from .models import Menu
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
from datetime import datetime, timedelta


class MenuList(generic.ListView):
    model = Menu
    # decide by which order to sort later 
    queryset = Menu.objects.filter(status=1).order_by('')
    template_name = 'index.html'
    paginate_by = 6