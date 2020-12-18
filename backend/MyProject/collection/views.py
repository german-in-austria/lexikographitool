from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from .models import Collection
from .serializers import CollectionSerializer
from lexeme.models import Lexeme
from group.models import Group


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_collection(request):
    account = request.user
    print(account)
    collection = Collection(author=account)
    if request.method == 'POST':
        serializer = CollectionSerializer(collection, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_collections_by_owner(request):
    account = request.user
    collections = Collection.objects.filter(author=account)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_collections(request):
    account = request.user
    collections = Collection.objects.filter(
        Q(author=account) | Q(group__members =account)
        ).distinct()    
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_collection(request,collectionId):
    account = request.user
    try:
        collection = Collection.objects.get(id=collectionId)
    except Collection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    if account != collection.author and( collection.group == None or account not in collection.group.members.all()):
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)

@api_view(['PUT','DELETE',])
@permission_classes([IsAuthenticated,])
def add_or_remove_lexeme_to_collection(request, collectionId, lexemeId):
    account = request.user
    try:
        collection = Collection.objects.get(id=collectionId)
        lexeme = Lexeme.objects.get(id=lexemeId)
    except Lexeme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Collection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    print(collection.group)
    if account != collection.author and( collection.group == None or account not in collection.group.members.all()):
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == 'PUT':
        collection.lexemes.add(lexeme)
        collection.save()
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        collection.lexemes.remove(lexeme)
        return Response(status= status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def add_group_to_collection(request,collectionId,groupId):
    account = request.user
    try:
        collection = Collection.objects.get(id=collectionId)
        group = Group.objects.get(id=groupId)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if account != collection.author or account != group.owner:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        collection.group = group
        collection.save()
        serializer = CollectionSerializer(collection)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
