from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=20)
    genres_name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
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
