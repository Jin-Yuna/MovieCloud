from rest_framework import serializers
from ..models import Drop
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        model = User
        fields = ('pk', 'username', )
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Drop
        fields = ('pk', 'user', 'content', 'drop', )
        read_only_fields = ('article, ')