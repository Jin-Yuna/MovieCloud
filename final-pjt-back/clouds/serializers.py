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

# 디테일에 필요한 데이터만 출력되도록 구조가 정해지면 수정하기
class DropDretailSerializer(serializers.ModelSerializer):
    # comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class MovieForDropDeatailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    movie = MovieForDropDeatailSerializer()
    user = UserSerializer(read_only=True)
    comments = CommentSimpleSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Drop
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('drop', 'user')


# 카드에 필요한 데이터만 출력되도록 구조가 정해지면 수정하기
class DropCardSerializer(serializers.ModelSerializer):

    class MovieForDropCardSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    movie = MovieForDropCardSerializer()
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Drop
        fields = '__all__'
