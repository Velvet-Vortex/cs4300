from django.db import models
from django.conf import settings

# Movie: title, description, release date, duration
class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()

# Seat: seat number, booking status
class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.BooleanField()

# Booking: movie, seat, user, booking date
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    booking_date = models.DateTimeField()