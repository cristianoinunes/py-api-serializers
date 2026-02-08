from rest_framework import viewsets
from .models import Movie, MovieSession
from .serializers import MovieSerializer, MovieDetailSerializer
from .serializers import MovieSessionSerializer, MovieSessionDetailSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionSerializer
        return MovieSessionDetailSerializer
