from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('kakaoLogin/', views.kakaoLogin),
    path('kakao_user_info/<int:pk>/', views.kakaoInfo),
    path('profile/<int:pk>/', views.profile)
]
