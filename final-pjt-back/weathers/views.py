from movies.models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from weathers.serializers import MovieSerializer


weather = {
  800: [12, 14, 28], # 800 맑은 날
  801: [16, 878, 36, 37],# 8801 구름 조금
  80: [35, 10402],  # 880x 구름 많음
  6: [18, 10751, 99],    # 86xx: Snow
  2: [80, 27, 9648, 53, 10752],  # 8Group 2xx: Thunderstorm
  7: [35, 10402],  # 87xx: Atmosphere
  5: [10749, 10770],   # 8Group 3xx: Drizzle, Group 5xx: Rain
  3: [10749, 10770]
}

@api_view(['GET'])
def weathers(request, pk):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    data = serializer.data
    
    based_num = pk // 100
    if based_num == 8:
        if pk == 800:
            based_num = 800
        elif pk == 801:
            based_num = 801
        else:
            based_num = 80
    genre = weather[based_num]

    response = []
    for i in range(len(data)):    
        for j in range(len(data[i]['genres'])):
            if data[i]['genres'][j] in genre:
                response.append(data[i])
                break
    print(response)
    return Response(response)
