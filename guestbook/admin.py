from django.contrib import admin
from guestbook.models import GuestBook


@admin.register(GuestBook)
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'created_at', 'status']
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['name', 'text']
    fields = ['name', 'email', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at']
