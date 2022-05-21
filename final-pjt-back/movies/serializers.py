from rest_framework import serializers
from .models import Movie


class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'movie_id', 'title', )
