from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('dish_name', 'price', 'status')
    list_filter = ('status', 'price')
    summernote_fields = ('content')

