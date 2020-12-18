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
from .serializers import *
from .models import *

from rest_framework.decorators import api_view

# Lexeme
def get_lexeme_by_id(id):
    try:
        return Lexeme.objects.get(id=id)
    except Lexeme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def card_list(request):
    if request.method == 'GET':
        cards = Lexeme.objects.all()
        serializers = CardSerializer(cards, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def get_lexeme(request, lexemeId):
    if request.method == 'GET':
        lexeme = get_lexeme_by_id(lexemeId)
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


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_lexeme(request):
    account = request.user
    print(account)
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
@permission_classes([IsAuthenticated,])
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

#Etymology
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_etymology(request):
    if request.method == 'POST':
        serializer = EtymologySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Pronunciation
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_pronunciation(request):
    if request.method == 'POST':
        serializer = PronunciationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Example
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_example(request):
    if request.method == 'POST':
        serializer = ExampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Category
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_category(request, pk):
    lexeme = Lexeme.objects.get(pk=pk)
    print(request.data)
    category, created = Category.objects.get_or_create(category=request.data['category'])
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
        Q(place__icontains=zip_or_place)
    )
    print(addresses[0].place)
    serializers = ZipPlaceSerializer(addresses, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)
