from django.urls import path
from .views import CreateBooking, RoomAvailability, GetBooked

urlpatterns = [
    path('create-booking/', CreateBooking.as_view(), name='create-booking'),
    path('room-availability/', RoomAvailability.as_view(), name='room-availability'),
    path('get-booked/', GetBooked.as_view(), name='get-booked'),
]
