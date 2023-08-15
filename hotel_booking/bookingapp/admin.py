from django.contrib import admin
from bookingapp.models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'category', 'rate']

admin.site.register(Room, RoomAdmin)

class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'user_name','check_in','check_out']

admin.site.register(Booking, RoomBookingAdmin)