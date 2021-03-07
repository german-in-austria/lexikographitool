from rest_framework import serializers

from .models import Lexeme, Address, Category, Example, Pronunciation, Etymology, LikeLexeme, LexemeContent
from rest_framework.fields import CurrentUserDefault
from django.db.models import Q
# Category
from collection.models import Collection,CollectionLexeme


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



# Lexeme




class LexemeDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True, validators=[])
    examples = ExampleSerializer(many=True, read_only=True)
    etymologies = EtymologySerializer(many=True, read_only=True)
    pronunciations = PronunciationSerializer(many=True, read_only=True)
    origin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lexeme
        fields = ['id', 'word', 'dialectWord', 'kind', 'description', 'origin',
                  'dialect', 'categories', 'etymologies', 'examples', 'pronunciations','sensitive']

        extra_kwargs = {
            'category': {'validators': []},
        }

    def get_username_from_author(selfself, lexeme):
        username = lexeme.author.username
        return username

    def get_origin(self, obj):
        if obj.origin == None:
            return None
        return obj.origin.state


class LexemeContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LexemeContent
        fields = ['id', 'description', 'dialect', 'kind', 'origin', 'word', 'dialectWord', 'sensitive','lexeme','variety']
       

class LexemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        fields = ['id','content']

        extra_kwargs = {
            'category': {'validators': []},
        }

    def get_username_from_author(self, lexeme):
        username = lexeme.author.username
        return username

    def get_origin(self, obj):
        
        if obj.origin == None:
            return None
        return obj.origin.state


# class OLDCardSerializer(serializers.ModelSerializer):
#     origin = serializers.SerializerMethodField(read_only=True)
#     liked = serializers.SerializerMethodField(read_only=True)
#     examples = ExampleSerializer(read_only=True, many=True)
#     pronunciations = PronunciationSerializer(read_only=True, many=True)
#     etymologies = EtymologySerializer(read_only=True,many=True)
#     categories = CategorySerializer(read_only=True, many=True)
#     in_favorites = serializers.SerializerMethodField(read_only=True)
#     in_collection = serializers.SerializerMethodField(read_only=True)
#     author = serializers.SerializerMethodField(read_only=True)
#     is_author = serializers.SerializerMethodField(read_only=True)

#     def get_origin(self, obj):
        
#         if obj.origin == None:
#             return None
#         return obj.origin.state

#     class Meta:
#         model = Lexeme
#         fields = '__all__'

#     def get_liked(self,card):
#         request = self.context.get("request")
#         if request and hasattr(request, "user") and hasattr(request.user, "favorite"):
#             account = request.user
#             like = LikeLexeme.objects.filter(Q(lexeme=card) & Q(user=account))
        
#             if len(like) != 0:
#                 return like[0].like

#         return False

#     def get_in_favorites(self, card):

#         request = self.context.get("request")
#         if request and hasattr(request, "user") and hasattr(request.user, "favorite"):
#             user = request.user

#             # TODO: Rauslöschen
#             if user and not hasattr(user.favorite, "lexemes"):
#                 favorite = Collection(name='Favoriten', author=user)
#                 favorite.save()
#                 user.favorite = favorite
#                 user.save()
#             if user.favorite.lexemes.filter(id=card.id).exists():
#                 return True

#         return False

#     def get_in_collection(self, card):
#         if 'collectionId' in self.context:

#             collectionId = self.context['collectionId']
#         else:
#             return None
#         if CollectionLexeme.objects.filter(Q(collection=collectionId)&Q(lexeme=card)).exists():

#             return True

#     def get_author(self, card):
#         print('######author#######')
#         print(card.author)
#         return card.author.username

#     def get_is_author(self, card):
#         if 'request' in self.context:
#             request = self.context['request']
#             if request.user == card.author:
#                 return True
#         return False


class CardSerializer(serializers.ModelSerializer):
    # content = serializers.SerializerMethodField(read_only=True)
    # origin = serializers.SerializerMethodField(read_only=True)
    # liked = serializers.SerializerMethodField(read_only=True)
    # examples = ExampleSerializer(read_only=True, many=True)
    # pronunciations = PronunciationSerializer(read_only=True, many=True)
    # etymologies = EtymologySerializer(read_only=True,many=True)
    word = serializers.SerializerMethodField(read_only=True)
    variety = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    kind = serializers.SerializerMethodField(read_only=True)
    dialectWord = serializers.SerializerMethodField(read_only=True)
    origin = serializers.SerializerMethodField(read_only=True)
    sensitive = serializers.SerializerMethodField(read_only=True)
    examples = serializers.SerializerMethodField(read_only=True)
    pronunciations = serializers.SerializerMethodField(read_only=True)
    etymologies = serializers.SerializerMethodField(read_only=True)
    categories = serializers.SerializerMethodField(read_only=True)

    author = serializers.SerializerMethodField(read_only=True)


    # categories = CategorySerializer(
    in_favorites = serializers.SerializerMethodField(read_only=True)
    in_collection = serializers.SerializerMethodField(read_only=True)
    # author = serializers.SerializerMethodField(read_only=True)
    is_author = serializers.SerializerMethodField(read_only=True)


    


    class Meta:
        model = Lexeme
        fields = '__all__'

    def get_word(self, obj):
        return obj.content.word

    def get_variety(self, obj):
        return obj.content.variety
    def get_description(self, obj):
        return obj.content.description
    def get_kind(self, obj):
        return obj.content.kind
    def get_dialectWord(self, obj):
        return obj.content.dialectWord
    def get_sensitive(self, obj):
        return obj.content.sensitive
    def get_examples(self, obj):
        return ExampleSerializer(obj.content.examples, many=True).data
    def get_pronunciations(self, obj):
        return PronunciationSerializer(obj.content.pronunciations, many=True).data
    def get_categories(self, obj):
        return CategorySerializer(obj.content.categories, many=True).data
    def get_etymologies(self, obj):
        return EtymologySerializer(obj.content.etymologies, many=True).data
    


    def get_origin(self, obj):
        content =  obj.versions.all().order_by('-date_created')[0]
        if content.origin == None:
            return None
        return content.origin.state

    
    def get_liked(self,card):
        request = self.context.get("request")
        if request and hasattr(request, "user") and hasattr(request.user, "favorite"):
            account = request.user
            like = LikeLexeme.objects.filter(Q(lexeme=card) & Q(user=account))
        
            if len(like) != 0:
                return like[0].like

        return False

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
        if CollectionLexeme.objects.filter(Q(collection=collectionId)&Q(lexeme=card)).exists():

            return True

    def get_author(self, card):
        
        return card.author.username

    def get_is_author(self, card):
        if 'request' in self.context:
            request = self.context['request']
            if request.user == card.author:
                return True
        return False


class LexemeSimpleSerializer(CardSerializer):
    class Meta:
        model = Lexeme
        fields = ['id','word','dialectWord','description']
