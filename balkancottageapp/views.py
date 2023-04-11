from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
from datetime import datetime, timedelta

