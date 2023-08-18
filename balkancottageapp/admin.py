from django.contrib import admin
from .models import Menu, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('dish_name', 'status')
    list_filter = ('status', 'dish_name')
    summernote_fields = ('content')


@admin.register(Reservation)
class ReservationOverview(admin.ModelAdmin):
    list_display = ('user', 'reservation_date', 'reservation_time', 'message')