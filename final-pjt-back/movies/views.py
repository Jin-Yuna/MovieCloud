from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts import serailizers

from movies.models import Movie
from .serializers import MovieSearchSerializer, MovieTitleSerializer

@api_view(['GET']) # 임시로 목록 조회랑 같이 둠.
def get_movie_title(request):
    if request.method == 'GET':
        movies_title = Movie.objects.values('pk', 'title')
        serializer = MovieTitleSerializer(movies_title, many=True)
        return Response(serializer.data)
        
@api_view(['GET'])
def get_movie_search(request):
    movie = Movie.objects.values('id', 'title')
    serailizer = MovieSearchSerializer(movie, many=True)
    print(serailizer.data)
    return Response(serailizer.data)
