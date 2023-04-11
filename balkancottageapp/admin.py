from django.contrib import admin
from .models import Menu
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
