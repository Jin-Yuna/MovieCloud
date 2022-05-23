from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from .models import Drop
from .serializers import (
    CommentSimpleSerializer,
    DropCreateSerializer,
    DropDretailSerializer,
    DropListSerializer,
    CommentListSerializer,
    CommentCreateSerializer,
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
    print('요청옴')
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
        print('수정요청')
        serializer = DropCreateSerializer(drop, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        drop.delete()
        return Response({'message': f'{pk}번 Drop이 삭제 되었습니다.'}, HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 로그인 한 사용자만 댓글달기 가능
def comment_create(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(drop=drop, user=request.user)
        comments = drop.comments.all()
        serializer = CommentSimpleSerializer(comments, many=True)
        return Response(serializer.data, HTTP_201_CREATED)