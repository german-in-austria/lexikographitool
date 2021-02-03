from rest_framework import serializers

from .models import Collection
from lexeme.serializers import LexemeDetailSerializer



class CollectionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_by_author')
    lexemes = LexemeDetailSerializer(many=True, read_only=True)
    can_add_lexeme_to_collection = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ['id','name', 'username', 'lexemes','group', 'description','organization', 'public','categories','can_add_lexeme_to_collection']

    def get_username_by_author(self, collection):
        username = collection.author.username
        return username

    def get_can_add_lexeme_to_collection(self, collection):

        if 'account' in self.context:
            user = self.context['account']
            if collection.group == None:
                return user == collection.author
            settings = collection.group.settings

            return user==collection.author or user == collection.group.owner or \
                   user in collection.group.members.all() and settings.members_add_remove_lexemes or \
                   settings.public and settings.public_add_remove_lexemes
        return False

class CollectionSimpleSerializer(serializers.ModelSerializer):
    groupname = serializers.SerializerMethodField('get_group_name')
    count_lexemes = serializers.SerializerMethodField('get_count_lexemes')

    class Meta:
        model = Collection
        fields = ['id','name', 'description','groupname','count_lexemes']

    def get_group_name(self, collection):
        if(collection.group):
            return collection.group.name
        return None

    def get_count_lexemes(self, collection):
        return collection.lexemes.count()


class CollectionSimpleSerializerWithContainment(serializers.ModelSerializer):
    in_collection = serializers.SerializerMethodField('ifcontained')
    class Meta:
        model = Collection
        fields = ['id','name', 'description' ,'in_collection']

    def ifcontained(self, collection):
        if collection.lexemes.filter(id=self.context['lexeme_id']).exists():
            return True
        return False