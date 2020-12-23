from rest_framework import serializers

from .models import Collection
from lexeme.serializers import LexemeDetailSerializer


class CollectionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_by_author')
    lexemes = LexemeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ['id','name', 'username', 'lexemes','group', 'description']

    def get_username_by_author(self, collection):
        username = collection.author.username
        return username

class CollectionSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id','name', 'description']
