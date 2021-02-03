from rest_framework import serializers

from .models import Post
from account.serializers import UserNameSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()
    # children = serializers.ListSerializer(read_only=True, child=RecursiveField())
    children = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'text', 'parent', 'author', 'children']

    def get_children(self, obj):
        children = Post.objects.filter(parent=obj)
        return PostSerializer(obj.children, many=True).data
        

class PostSimpleSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()

    class Meta:
        model = Post
        fields = ['id', 'text', 'author']

class PostCreateSerializer(serializers.ModelSerializer):
    author = UserNameSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'text', 'parent', 'author', 'lexeme']