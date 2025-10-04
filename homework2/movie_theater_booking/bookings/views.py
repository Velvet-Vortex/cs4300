from rest_framework import viewsets
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows movies to be created, retrieved, updated, and destroyed
    '''
    queryset = Movie.objects.all()

class SeatViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    '''
    API endpoint that allows seats to be retrieved and updated
    '''
    queryset = Seat.objects.all()

class BookingViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    API endpoint that allows bookings to be created and retrieved
    '''
    queryset = Booking.objects.all()