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
    DropCreateSerializer,
    DropDretailSerializer,
    DropListSerializer,
    CommentListSerializer,
    CommentCreateSerializer
)

@api_view(['GET', 'POST']) # 임시로 목록 조회랑 같이 둠.
def drop_create(request):
    if request.method == 'GET':
        drops = Drop.objects.annotate(comment_count=Count('comments', distinct=True)).order_by('-pk')
        serializer = DropListSerializer(drops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DropCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, HTTP_201_CREATED)


@api_view(['GET'])
def drop_detail(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    if request.method == 'GET':
        serializer = DropDretailSerializer(drop)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def drop_edit_delete(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    if request.method == 'PUT':
        serializer = DropCreateSerializer(drop, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        drop.delete()
        return Response({'message': f'{pk}번 Drop이 삭제 되었습니다.'}, HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comment_list_create(request, pk):
    drop = get_object_or_404(Drop, pk=pk)
    if request.method == 'GET':
        comments = get_list_or_404(drop.comment_set.order_by('-pk'))
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(drop=drop, user=request.user)
            return Response(serializer.data, HTTP_201_CREATED)