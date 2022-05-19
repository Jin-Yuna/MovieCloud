from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Drop
from .comment import CommentSerializer

User = get_user_model()

class DropSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        model = User
        fields = ('pk', 'username', )

    class Meta:
        model = Drop
        fields = ('pk', 'user', 'title', )