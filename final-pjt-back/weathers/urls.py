from django.urls import path
from . import views

app_name='weathers'

urlpatterns = [
    path('<int:pk>/', views.weathers),
]
