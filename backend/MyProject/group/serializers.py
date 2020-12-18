
from .models import Group
from account.serializers import UserNameSerializer
from collection.serializers import CollectionSerializer
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    members = UserNameSerializer(many=True, read_only=True)
    collections = CollectionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id','name','description', 'members','collections']
