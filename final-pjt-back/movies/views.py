from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.models import Movie
from .serializers import MovieTitleSerializer

@api_view(['GET']) # 임시로 목록 조회랑 같이 둠.
def get_movie_title(request):
    if request.method == 'GET':
        movies_title = Movie.objects.values('pk', 'movie_id', 'title')
        serializer = MovieTitleSerializer(movies_title, many=True)
        return Response(serializer.data)


