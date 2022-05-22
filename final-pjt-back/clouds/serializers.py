from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Drop, Comment
from movies.models import Movie

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', )


class DropListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drop
        fields = '__all__'


class DropCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drop
        fields = (
            'movie',
            'title',
            'content',
            'user_vote',
        )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class CommentSimpleSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.username', read_only = True)
    class Meta:
        model = Comment
        fields = ('user_name', 'content', )


class DropDretailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    comments = CommentSimpleSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    # like_users = serializers.CharField(source='user.username', read_only = True)
    class Meta:
        model = Drop
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('drop', 'user')