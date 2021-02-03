from django.db.models import Q
from rest_framework.filters import SearchFilter

from .serializers import PostSerializer, PostSimpleSerializer, PostCreateSerializer
from .models import Post
from rest_framework.response import Response

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes, api_view


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_post(request):
    account = request.user
    post = Post(author=account)
    if request.method == 'POST':
        serializer = PostCreateSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_post_by_id(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializers = PostSerializer(post)
        return Response(serializers.data)

@api_view(['GET'])
def get_post_by_lexemes(request, lexemeId):
    if request.method == 'GET':
        posts = Post.objects.filter(lexeme=lexemeId)
        serializers = PostSimpleSerializer(posts, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def get_posts(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            posts = Post.objects.filter(Q(parent=None) & Q(lexeme=None) & (Q(text__icontains= request.GET['search'])))
        else:
            posts = Post.objects.filter(Q(parent=None) & Q(lexeme=None))
        serializers = PostSimpleSerializer(posts, many=True)
        return Response(serializers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_own_posts(request):
    account = request.user
    if request.method == 'GET':
        posts = Post.objects.filter(Q(parent=None) & Q(lexeme=None) & Q(author=account))
        serializers = PostSimpleSerializer(posts, many=True)
        return Response(serializers.data)


