from rest_framework import serializers

from .models import Article, Lexeme, DialectWord, Address, Category, Example, Pronunciation, Etymology, Dialect
from rest_framework.fields import CurrentUserDefault

# Category
from collection.models import Collection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

        extra_kwargs = {
            'category': {'validators': []},
        }


# Address
class ZipPlaceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ['id', 'zipcode', 'place', 'state']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'state']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# Example
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'


# Pronunciation
class PronunciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronunciation
        fields = '__all__'


# Etymology
class EtymologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Etymology
        fields = '__all__'


# Dialect


class DialectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialect
        fields = '__all__'


# Lexeme


class LexemeSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        fields = ['word']


class LexemeDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True, validators=[])
    examples = ExampleSerializer(many=True, read_only=True)
    etymologies = EtymologySerializer(many=True, read_only=True)
    pronunciations = PronunciationSerializer(many=True, read_only=True)
    origin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lexeme
        fields = ['id', 'word', 'dialectWord', 'kind', 'description', 'origin',
                  'dialect', 'categories', 'etymologies', 'examples', 'pronunciations']

        extra_kwargs = {
            'category': {'validators': []},
        }

    def get_username_from_author(selfself, lexeme):
        username = lexeme.author.username
        return username

    def get_origin(self, obj):
        return obj.origin.state


class LexemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        fields = ['id', 'description', 'dialect', 'kind', 'origin', 'word', 'dialectWord']

        extra_kwargs = {
            'category': {'validators': []},
        }

    def get_username_from_author(self, lexeme):
        username = lexeme.author.username
        return username

    def get_origin(self, obj):
        return obj.origin.state


class CardSerializer(serializers.ModelSerializer):
    origin = serializers.SerializerMethodField(read_only=True)
    examples = ExampleSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    in_favorites = serializers.SerializerMethodField(read_only=True)
    in_collection = serializers.SerializerMethodField(read_only=True)

    def get_origin(self, obj):
        return obj.origin.state

    class Meta:
        model = Lexeme
        fields = '__all__'

    def get_in_favorites(self, card):

        request = self.context.get("request")
        if request and hasattr(request, "user") and hasattr(request.user, "favorite"):
            user = request.user

            # TODO: Rauslöschen
            if user and not hasattr(user.favorite, "lexemes"):
                favorite = Collection(name='Favoriten', author=user)
                favorite.save()
                user.favorite = favorite
                user.save()
            if user.favorite.lexemes.filter(id=card.id).exists():
                return True

        # if collection.lexemes.filter(id=self.context['lexeme_id']).exists():
        #    return True
        return False

    def get_in_collection(self, card):
        if 'collectionId' in self.context:
            collectionId = self.context['collectionId']
        else:
            return None
        if card.collections.filter(id=collectionId).exists():
            return True
        return False
