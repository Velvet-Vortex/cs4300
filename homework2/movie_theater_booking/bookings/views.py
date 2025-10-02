from rest_framework import viewsets
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows movies to be created, viewed, edited, and destroyed (CRUD)
    '''
    queryset = Movie.objects.all()