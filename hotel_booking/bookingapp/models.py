from django.db import models

class Room(models.Model):
    CATEGORY_CHOICES = [
        ('Deluxe', 'Deluxe Rooms - Queen Size Bed'),
        ('Luxury', 'Luxury Rooms - Queen Size Bed and Pool Facing'),
        ('Suite', 'Luxury Suites - King Size Bed and Pool Facing'),
        ('Presidential', 'Presidential Suites - King Size Bed, Pool Facing with a Gym'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    room_number = models.CharField(max_length=5)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.category} - Room {self.room_number}"

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user_name} - {self.room} ({self.check_in} to {self.check_out})"
