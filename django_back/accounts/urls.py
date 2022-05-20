from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('kakaoLogin/', views.kakaoLogin),
    path('kakaoLogin/callback/', views.kakaoLoginCallback),
]
