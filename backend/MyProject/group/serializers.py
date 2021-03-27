from .models import Group, GroupSettings
from account.serializers import UserNameSerializer
from collection.serializers import CollectionSerializer, CollectionSimpleSerializerWithContainment
from rest_framework import serializers
from MyProject import rulemanager

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
    is_owner = serializers.SerializerMethodField('check_if_owner')

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'members', 'collections', 'owner', 'is_owner', 'can_create_collection',
                  'organization']

    def check_if_owner(self, group):
        if 'account' in self.context:
            return self.context['account'] == group.owner
        return False

    def get_can_create_collection(self,group):
        user = None
        if 'account' in self.context:
            user = self.context['account']
        
        return rulemanager.can_add_collection_to_group(group,user)


class GroupNameSerializer(serializers.ModelSerializer):
    requires_password = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name','requires_password']

    def get_requires_password(self, group):
        return group.settings.need_password

class GroupCollectionSerializer(serializers.ModelSerializer):
    collections = CollectionSimpleSerializerWithContainment(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'collections']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We pass the "upper serializer" context to the "nested one"
        self.fields['collections'].context.update(self.context)
