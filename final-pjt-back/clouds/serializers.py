from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Drop, Comment
from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', )

class MovieAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


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
    # comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Drop
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('drop', 'user')


class DropCardSerializer(serializers.ModelSerializer):
    movie = MovieAllSerializer()
    comments = CommentSimpleSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Drop
        fields = '__all__'
