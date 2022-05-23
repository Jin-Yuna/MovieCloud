from movies import models
from rest_framework.decorators import api_view
from rest_framework.response import Response


weather = {
    800: [',모험', '판타지', '액션'], # 800 맑은 날
    801: ['애니메이션', 'SF', '역사', '서부'], # 801 구름 조금
    80: ['코미디', '음악'],  # 80x 구름 많음
    6: ['드라마', '가족', '다큐멘터리'],    # 6xx: Snow
    2: ['범죄', '공포', '미스터리', '스릴러', '전쟁'],  # Group 2xx: Thunderstorm
    7: ['코미디', '음악'],  # 7xx: Atmosphere
    5: ['로맨스', 'TV 영화'],   # Group 3xx: Drizzle, Group 5xx: Rain
    3: ['로맨스', 'TV 영화']
}

@api_view(['GET'])
def weathers(request, pk):
    Movies = models.Movie.objects.all()
    based_num = pk // 100
    if based_num == 8:
        if pk == 800:
            based_num = 800
        elif pk == 801:
            based_num = 801
        else:
            based_num = 80
    genres = weather[based_num]
    response = []
    for Movie in Movies:
        movies = Movies.split(',')
        print(movies)
        for i in range(Movie.genres.length):

            if Movie.genres[i] in genres:
                print(Movie.genres[i])
                response.append(Movie)
                break
    print(response)
    return Response(response)
