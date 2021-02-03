from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters

from .pagination import MyPagination
from .serializers import *
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
import random


# Lexeme

@api_view(['GET'])
def card_list(request):
    if request.method == 'GET':
        cards = Lexeme.objects.all()
        serializers = CardSerializer(cards, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def get_random_lexemes(request):
    if request.method == 'GET':
        lexeme_id_list = Lexeme.objects.all().values_list('id', flat=True)
        print(lexeme_id_list)

        random_lexeme_list = random.sample(list(lexeme_id_list), min(len(lexeme_id_list), 5))

        cards = list(Lexeme.objects.filter(id__in=random_lexeme_list))
        random.shuffle(cards)
        serializers = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializers.data)


@api_view(['GET'])
def card_list(request):
    if request.method == 'GET':
        cards = Lexeme.objects.all()
        serializers = CardSerializer(cards, many=True)
        return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def card_own(request):
    account = request.user
    if request.method == 'GET':
        cards = Lexeme.objects.filter(author=account)
        serializers = CardSerializer(cards, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def get_lexeme(request, lexemeId):
    if request.method == 'GET':
        try:
            lexeme = Lexeme.objects.get(id=lexemeId)
        except Lexeme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers = LexemeDetailSerializer(lexeme)
        return Response(serializers.data)


@api_view(['GET'])
def lexeme_first_by_word(request, word):
    lexemes = Lexeme.objects.filter(word=word)
    if len(lexemes) != 0:
        serializer = LexemeDetailSerializer(lexemes[0])
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class LexemeListView(ListAPIView):
    queryset = Lexeme.objects.all()
    serializer_class = LexemeSimpleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['word']


class LexemeView(ListAPIView):
    queryset = Lexeme.objects.all()
    serializer_class = CardSerializer
    pagination_class = MyPagination
    pagination_class.page_size = 14
    filter_backends = [SearchFilter]
    search_fields = ['word', 'dialectWord']

    def get_serializer_context(self):
        collection = -1
        if 'collection' in self.request.GET:
            collection = self.request.GET['collection']
        context = super(LexemeView, self).get_serializer_context()
        context.update({"request": self.request, "collectionId": collection}, )
        return context


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_lexeme(request):
    account = request.user
    lexeme = Lexeme(author=account)
    if request.method == 'POST':
        serializer = LexemeCreateSerializer(lexeme, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Dialect
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_dialect(request):
    if request.method == 'POST':
        try:
            dialect = Dialect.objects.get(dialect=request.data['dialect'])
        except Dialect.DoesNotExist:
            serializer = DialectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = DialectSerializer(dialect)
        return Response(serializer.data)


class DialectListView(ListAPIView):
    queryset = Dialect.objects.all()
    serializer_class = DialectSerializer
    filter_backends = [SearchFilter]
    search_fields = ['dialect']


# Etymology


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_etymology(request):
    if request.method == 'POST':
        serializer = EtymologySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Pronunciation


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_pronunciation(request):
    if request.method == 'POST':
        serializer = PronunciationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Example
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_example(request):
    if request.method == 'POST':
        serializer = ExampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Category


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_category(request, pk):
    lexeme = Lexeme.objects.get(pk=pk)
    print(request.data)
    category, created = Category.objects.get_or_create(
        category=request.data['category'])
    print(category)
    serializer = CategorySerializer(category)
    category.lexemes.add(lexeme)
    if created:
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['category']


# Origin


@api_view(['GET'])
def origin_by_zip_or_place(request, zip_or_place):
    addresses = Address.objects.filter(
        Q(place__icontains=zip_or_place) | Q(zipcode__startswith=zip_or_place)
    )
    print(addresses[0].place)
    serializers = ZipPlaceSerializer(addresses, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_home(request):
    account = request.user
    location = account.home
    serializers = ZipPlaceSerializer(location)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_address(request):
    if request.method == 'POST':
        serializer = ZipPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_locations(request):
    if request.method == 'GET':
        if 'zip' in request.GET:
            locations = Address.objects.filter(zipcode__startswith=request.GET['zip'])
        elif 'place' in request.GET:
            locations = Address.objects.filter(place__icontains=request.GET['place'])
        else:
            return Response()
    serializers = ZipPlaceSerializer(locations, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)
