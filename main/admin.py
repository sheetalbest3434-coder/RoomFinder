from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'rent', 'contact_number', 'owner', 'created_at')
