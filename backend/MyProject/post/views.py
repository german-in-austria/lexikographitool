from .serializers import PostSerializer, PostSimpleSerializer, PostCreateSerializer
from .models import Post
from rest_framework.response import Response

from rest_framework import status
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
def get_posts(request):
    if request.method == 'GET':
        posts = Post.objects.filter(parent=None)
        serializers = PostSimpleSerializer(posts, many=True)
        return Response(serializers.data)
