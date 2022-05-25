from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    path('profile/<int:pk>/', views.profile),
    path('kakaoLogin/', views.kakaoLogin),
    path('follow/<int:pk>/', views.follow),
]
