# movies에 관한 data를 json파일로

## 1. 어려움

### 1. tmdb에 요청을 많이 보냈더니 응답이 안오게 되었음

- 500(popular) + 10,000(detail)번의 요청을 보내고 있었는데, 갑자기 응답이 안오게 됨
- 이전에 코드를 짜면서 보냈던 요청들까지 합쳐 너무 많은 요청을 보내서 이렇게 된 것으로 추정.



### 2. dumpdata 오류

- 우선 저장된 200개의 데이터라도 시험용으로 dumpdata를 사용하여 json 파일로 만들어보려 하였으나, 오류 발생

  ```bash
  python manage.py dumpdata DB.Movies --indent 4 > movies.json
  ```

  \><span style="color:red">sqlite3.ProgrammingError: Cannot operate on a closed database.</span>

- json파일에 일부 저장된 내용의 한글 깨짐 현상

  ```json
  {
      "model": "DB.movies",
      "pk": 1,
      "fields": {
          "movie_id": 675353,
          "title":    
          "genres": "�׼�, SF, �ڹ̵�, ����, ����, ",
          "release_date": "2022-03-30",
          "poster_path": "/8dzKn3RtPWUJRG9ymSpi423eMNV.jpg",
          "overview": "������ �Ŀ��� ����Ŭ��� �Բ� ���ƿ� õ�� ������ ������ �κ�Ʈ�С��� �¼� ������ ���ϱ� ���� ���ҴС��� ���ο� ��Ʈ�� ��������� �� ���踦 ����� ���ǵ� �׼� ���Ϲ�����.",
          "tagline": "",
          "adult": false,
          "backdrop_path": "/egoyMDLqCxzjnSrWOz50uLlJWmD.jpg",
          "budget": 110000000,
          "original_language": "en",
          "original_title": "Sonic the Hedgehog 2",
          "popularity": 7375.149,
          "production_countries": "Japan",
          "revenue": 355200000,
          "runtime": 122,
          "spoken_languages": "English",
          "vote_average": 7.7,
          "vote_count": 1436
      }
  },
  ```



## 2. 응답 데이터 예시(detail)

- 우선 모델에 넣을 데이터는 앞에 [v]표시함

```json
{
[v] "adult": false,  
[v] "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg", 
[v] "belongs_to_collection": null,
[0] "budget": 63000000, 
    "genres": [
        {
        "id": 18,
[v]     "name": "Drama"   
        }
    ],
    "homepage": "",
    "id": 550,
    "imdb_id": "tt0137523",
[v] "original_language": "en",
[v] "original_title": "Fight Club",
[v] "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
[v] "popularity": 0.5,
[v] "poster_path": null,
    "production_companies": [
        {
        "id": 508,
        "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
[v]     "name": "Regency Enterprises",
        "origin_country": "US"
        },
        {
        "id": 711,
        "logo_path": null,
        "name": "Fox 2000 Pictures",
        "origin_country": ""
        },
        {
        "id": 20555,
        "logo_path": null,
        "name": "Taurus Film",
        "origin_country": ""
        },
        {
        "id": 54050,
        "logo_path": null,
        "name": "Linson Films",
        "origin_country": ""
        },
        {
        "id": 54051,
        "logo_path": null,
        "name": "Atman Entertainment",
        "origin_country": ""
        },
        {
        "id": 54052,
        "logo_path": null,
        "name": "Knickerbocker Films",
        "origin_country": ""
        },
        {
        "id": 25,
        "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
        "name": "20th Century Fox",
        "origin_country": "US"
        }
    ],
    "production_countries": [
        {
        "iso_3166_1": "US",
[v]     "name": "United States of America"
        }
    ],
[v] "release_date": "1999-10-12",
[0] "revenue": 100853753,
[v] "runtime": 139,
    "spoken_languages": [
        {
[v]     "iso_639_1": "en",
[0]     "name": "English"
        }
    ],
    "status": "Released",
[v] "tagline": "How much can you know about yourself if you've never been in a fight?",
[v] "title": "Fight Club",
    "video": false,
[v] "vote_average": 7.8,
[v] "vote_count": 3439
}
```



## 3. 코드

### 1. models.py : key를 move_id로 하려다 그냥 필드로 따로 만들어줬습니다.

```python
# dumpdata할때 뭐가 자꾸 오류가 나서 비어있으면 안되는 필드도 null=True로 우선 해둠.
class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=20)
    genres = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    poster_path = models.CharField(max_length=150, null=True)
    overview = models.TextField()
    tagline = models.TextField(null=True)
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=150, null=True)
    original_language = models.CharField(max_length=5)
    original_title = models.CharField(max_length=30)
    popularity = models.FloatField(null=True)
    production_countries = models.CharField(max_length=20)
    runtime = models.IntegerField(null=True)
    spoken_languages = models.CharField(max_length=10)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    production_companies = models.TextField(null=True)
    video_key = models.CharField(max_length=40, null=True)
```



### 2. views.py (모델 수정 전)

```python
import requests
from .models import Movies

TMDB_API_KEY = '*****' #DB만 받아올 앱이라 키 여기다 그냥 씀

def get_movie_datas(request):
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    # 너무 오래걸려서 10 페이지 씩 나눠서 요청해야겠음
    for i in range(1,11):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('id'):
                movie_id = movie['id']
                detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
                detail = requests.get(detail_url).json()
                title = detail['title']
                
                genres = ''
                for genre in detail['genres']:
                    genres += genre['name']+', '
                if detail['release_date']:
                    release_date = detail['release_date']
                poster_path = detail['poster_path']  # 'https://image.tmdb.org/t/p/w500' +poster_path
                overview = detail['overview']
                tagline = detail['tagline']
                adult = detail['adult']
                backdrop_path = detail['backdrop_path']
                budget = detail['budget']
                original_language = detail['original_language']
                original_title = detail['original_title']
                popularity = detail['popularity']
                if detail['production_countries']:
                    production_countries = detail['production_countries'][0]['name']
                revenue = detail['revenue']
                runtime = detail['runtime']
                if detail['spoken_languages']:
                    spoken_languages = detail['spoken_languages'][0]['name']
                vote_average = detail['vote_average']
                vote_count = detail['vote_count']

                my_movie = Movies()
                my_movie.movie_id  = movie_id
                my_movie.title = title
                my_movie.genres = genres
                my_movie.release_date = release_date
                my_movie.poster_path = poster_path
                my_movie.overview = overview
                my_movie.tagline = tagline
                my_movie.adult = adult
                my_movie.backdrop_path = backdrop_path
                my_movie.budget = budget
                my_movie.original_language = original_language
                my_movie.original_title = original_title
                my_movie.popularity = popularity
                my_movie.production_countries = production_countries
                my_movie.revenue = revenue
                my_movie.runtime = runtime
                my_movie.spoken_languages = spoken_languages
                my_movie.vote_average = vote_average
                my_movie.vote_count = vote_count
                my_movie.save()
```

### 3. views.py 수정

```python
from django.shortcuts import render
import requests
import json

TMDB_API_KEY = '*************' #DB만 받아올 앱이라 키 그냥 씀

def get_movie_datas(request):
    total_data = []
    for i in range(1,501):
        # 인기도에 따라 영화리스트 받기 : 한페이지 당 20개, 500페이지.
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            # print(movie['id'])
            movie_id = movie['id']
            # 받아온 리스트의 영화 아이디로 video 검색
            video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=ko-KR"
            videos = requests.get(video_url).json()
            
			# 비디오와 (한글)줄거리가 있는 데이터만 저장
            if videos['results'] and movie.get('overview'):
                # print(movie_id)
                video_key = videos['results'][0]['key']
                detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
                detail = requests.get(detail_url).json()
                genres = ''
                for genre in detail['genres']:
                    genres += genre['name']+', '
                # print(detail['title'], genres)
                if detail['release_date']:
                    release_date = detail['release_date']
                if detail['production_countries']:
                    production_countries = detail['production_countries'][0]['name']
                if detail['spoken_languages']:
                    spoken_languages = detail['spoken_languages'][0]['iso_639_1']
                production_companies = ''
                for production in detail['production_companies']:
                    production_companies += production['name'] + ', '
                    
                fields = {
                    'movie_id' : movie_id,
                    'title' : detail['title'],
                    'genres' : genres,
                    'release_date' : release_date, 
                    'poster_path' : detail['poster_path'],  # 'https://image.tmdb.org/t/p/w500' +poster_path
                    'overview' : detail['overview'],
                    'tagline' : detail['tagline'],
                    'adult' : detail['adult'],
                    'backdrop_path' : detail['backdrop_path'],
                    'original_language' : detail['original_language'],
                    'original_title' : detail['original_title'],
                    'popularity' : detail['popularity'],
                    'production_countries' : production_countries,
                    'runtime' : detail['runtime'],
                    'spoken_languages' : spoken_languages,
                    'vote_average' : detail['vote_average'],
                    'vote_count' : detail['vote_count'],
                    'production_companies' : production_companies,
                    'video_key': video_key,
                }
                data = {
                    "model" : "movies.movie", # 만들 앱과 모델 이름과 동일하게 해줘야 함.
                    "fields" : fields,
                }
                total_data.append(data)
    with open("movie_db.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)
```

## 4. 추가할 것

- video 필드, tmdb에서 movie_id로 검색
- https://developers.themoviedb.org/3/movies/get-movie-videos
