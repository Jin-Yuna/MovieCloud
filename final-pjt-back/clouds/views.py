from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from .models import Drop, Comment
from .serializers import (
    DropCreateSerializer,
    DropDretailSerializer,
    CommentSerializer,
    DropCardSerializer
)

@api_view(['GET'])
def drop_list(request):
    drops = Drop.objects.annotate(comment_count=Count('comments', distinct=True)).order_by('-pk')
    serializer = DropCardSerializer(drops, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 로그인 한 사용자만 글쓰기 가능
def drop_create(request):
    serializer = DropCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def drop_detail(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    if request.method == 'GET':
        serializer = DropDretailSerializer(drop)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = DropCreateSerializer(drop, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        drop.delete()
        return Response({'message': f'{pk}번 Drop이 삭제 되었습니다.'}, HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def like_drop(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    user = request.user
    if drop.like_users.filter(pk=user.pk).exists():
        drop.like_users.remove(user)
        serializer = DropDretailSerializer(drop)
        return Response(serializer.data)
    else:
        drop.like_users.add(user)
        serializer = DropDretailSerializer(drop)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 로그인 한 사용자만 댓글달기 가능
def create_comment(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer)
        serializer.save(drop=drop, user=request.user)
        comments = drop.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, HTTP_201_CREATED)



@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, pk, comment_pk):
    drop = get_object_or_404(Drop, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = drop.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            comments = drop.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    