from django.contrib import admin
from .models import Menu, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class PostAdmin(SummernoteModelAdmin):
    # Add later the filters and sorting methods after decision 
    # which layout the menu will have
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'content', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('user', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

