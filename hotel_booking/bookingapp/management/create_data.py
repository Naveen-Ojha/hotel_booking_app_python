from django.core.management.base import BaseCommand
from bookingapp.models import RoomCategory, Room

# create master data and users using Django management commands.
class Command(BaseCommand):
    help = 'Create master data'

    def handle(self, *args, **options):
        deluxe_category = RoomCategory.objects.create(name='Deluxe', price_per_night=7000)
        luxury_category = RoomCategory.objects.create(name='Luxury', price_per_night=8500)
        suite_category = RoomCategory.objects.create(name='Suite', price_per_night=12000)

        for i in range(1, 21):
            Room.objects.create(room_number=f'A{i:02}', category=deluxe_category)
            Room.objects.create(room_number=f'B{i:02}', category=deluxe_category)
            Room.objects.create(room_number=f'C{i:02}', category=deluxe_category)
            if i <= 10:
                Room.objects.create(room_number=f'D{i:02}', category=luxury_category)
                if i <= 2:
                    Room.objects.create(room_number=f'E{i:02}', category=suite_category)
