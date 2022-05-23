from rest_framework import serializers
from .models import User


class KakaoUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('pk', 'kakao_id', 'password', 'nickname', )

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname')