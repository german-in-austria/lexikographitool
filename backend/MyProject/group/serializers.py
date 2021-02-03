from .models import Group, GroupSettings
from account.serializers import UserNameSerializer
from collection.serializers import CollectionSerializer, CollectionSimpleSerializerWithContainment
from rest_framework import serializers


class GroupSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSettings
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    members = UserNameSerializer(many=True, read_only=True)
    collections = CollectionSerializer(many=True, read_only=True)
    owner = UserNameSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField('check_if_owner')
    can_create_collection = serializers.SerializerMethodField()
    can_add_lexeme_to_collection = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField('check_if_owner')

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members', 'collections', 'owner', 'is_owner', 'settings', 'can_create_collection', 'can_add_lexeme_to_collection',
                  'organization']

    def check_if_owner(self, group):
        if 'account' in self.context:
            return self.context['account'] == group.owner
        return False

    def get_can_create_collection(self,group):
        settings = group.settings

        if 'account' in self.context:
            user = self.context['account']
            return user == group.owner or \
                   user in group.members.all() and settings.members_createCollection or\
                   settings.public and settings.public_createCollection
        return False

    def get_can_add_lexeme_to_collection(self, group):
        settings = group.settings

        if 'account' in self.context:
            user = self.context['account']
            return user == group.owner or \
                   user in group.members.all() and settings.members_add_remove_lexemes or \
                   settings.public and settings.public_add_remove_lexemes
        return False


class GroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class GroupCollectionSerializer(serializers.ModelSerializer):
    collections = CollectionSimpleSerializerWithContainment(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'collections']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We pass the "upper serializer" context to the "nested one"
        self.fields['collections'].context.update(self.context)
