from rest_framework import serializers
from .models import Movie, Genre, Actor, MovieSession, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        slug_field="name", queryset=Genre.objects.all(), many=True)
    actors = serializers.SlugRelatedField(
        slug_field="__str__", queryset=Actor.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time",
                  "movie_title", "cinema_hall_name",
                  "cinema_hall_capacity"]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(read_only=True)
    cinema_hall = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
