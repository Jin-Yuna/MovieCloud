from rest_framework import serializers
from .models import User


class KakaoUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('kakao_id', 'password', 'nickname', )