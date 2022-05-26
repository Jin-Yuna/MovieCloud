from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts import serailizers

from movies.models import Movie
from .serializers import MovieSearchSerializer, MovieTitleSerializer

@api_view(['GET'])
def get_movie_title(request):
    movies_title = Movie.objects.values('pk', 'title')
    serializer = MovieTitleSerializer(movies_title, many=True)
    return Response(serializer.data)
        
@api_view(['GET'])
def get_movie_search(request):
    movie = Movie.objects.values('id', 'title')
    serailizer = MovieSearchSerializer(movie, many=True)
    return Response(serailizer.data)
