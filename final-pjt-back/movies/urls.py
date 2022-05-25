from django.urls import path
from . import views

urlpatterns = [
    path('get_movie_title/', views.get_movie_title),
    path('get_movie_search/', views.get_movie_search)   
]
