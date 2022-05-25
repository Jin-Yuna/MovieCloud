from rest_framework import serializers
from .models import User
from clouds.models import Drop
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class DropSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Drop
        fields = ('pk', 'title', 'content', 'movie')

class ProfileSerializer(serializers.ModelSerializer):
    like_drops = DropSerializer(many=True)
    drops = DropSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname', 'followings', 'followers', 'like_drops', 'drops',)