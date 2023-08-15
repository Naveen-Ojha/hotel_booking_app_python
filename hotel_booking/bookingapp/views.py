from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room, Booking
from datetime import datetime, timedelta

class CreateBooking(APIView):
    def post(self, request, format=None):
        # Extract data from the request
        room_id = request.data.get('room_id')
        user_name = request.data.get('user_name')
        check_in = datetime.strptime(request.data.get('check_in'), '%Y-%m-%d').date()
        check_out = datetime.strptime(request.data.get('check_out'), '%Y-%m-%d').date()

        try:
            room = Room.objects.get(pk=room_id)
        except Room.DoesNotExist:
            return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the room is available for the given dates
        conflicting_bookings = Booking.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in
        )
        if conflicting_bookings.exists():
            return Response({'error': 'Room is not available for the selected dates'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the booking
        booking = Booking(user_name=user_name, room=room, check_in=check_in, check_out=check_out)
        booking.save()
        return Response({'message': 'Booking created successfully'}, status=status.HTTP_201_CREATED)

class RoomAvailability(APIView):
    def get(self, request, format=None):
        category = request.query_params.get('category')
        date = datetime.strptime(request.query_params.get('date'), '%Y-%m-%d').date()

        rooms = Room.objects.filter(category=category)
        available_rooms = []

        for room in rooms:
            conflicting_bookings = Booking.objects.filter(
                room=room,
                check_in__lt=date + timedelta(days=1),
                check_out__gt=date
            )
            if not conflicting_bookings.exists():
                available_rooms.append(room)

        return Response({'available_rooms': [str(room) for room in available_rooms]})

class GetBooked(APIView):
    def get(self, request, format=None):
        booking_id = request.query_params.get('booking_id')
        try:
            booking = Booking.objects.get(pk=booking_id)
            return Response({
                'user_name': booking.user_name,
                'room': str(booking.room),
                'check_in': booking.check_in,
                'check_out': booking.check_out,
            })
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
