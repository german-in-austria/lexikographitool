from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import GroupSerializer, GroupSettingsSerializer
from .serializers import GroupNameSerializer
from .models import Group, GroupSettings
from account.models import Account
import hashlib
from django.contrib.sites.shortcuts import get_current_site


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def create_group(request):
    account = request.user
    group = Group(owner=account)
    if request.method == 'POST':
        serializer = GroupSerializer(group, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def add_or_remove_user(request, groupId, username):
    try:
        group = Group.objects.get(pk=groupId)
        member = Account.objects.get(username=username)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if group.owner != user:
        return Response({'response': 'You dont have permissions to add users to this group'},
                        status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        group.members.add(member)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    if request.method == 'DELETE':
        group.members.remove(member)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_own_groups(request):
    account = request.user

    groups = Group.objects.filter(
        Q(owner=account) | Q(members=account)
    ).distinct()
    serializers = GroupSerializer(groups, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated, ])
def get_update_group(request, groupId):
    account = request.user
    try:
        group = Group.objects.get(id=groupId)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if group.owner != account and account not in group.members.all():
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        serializer = GroupSerializer(group, context={'account': account})
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_invite_link(request, groupId):
    account = request.user
    try:
        group = Group.objects.get(id=groupId)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if group.owner != account:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    hash = hashlib.md5(group.__str__().encode())
    print(hash)
    return Response(hash.hexdigest())


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def join_group(request, groupId, hash):
    account = request.user
    try:
        group = Group.objects.get(id=groupId)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(hash)
    # print(hashlib.md5(group.__str__().encode()).hexdigest())
    if hash == hashlib.md5(group.__str__().encode()).hexdigest():
        group.members.add(account)
        group.save()
        return Response()
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_group_name_by_invite(request, groupId, hash):
    try:
        group = Group.objects.get(id=groupId)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if hash == hashlib.md5(group.__str__().encode()).hexdigest():
        return Response(GroupNameSerializer(group).data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated, ])
def get_update_group_settings(request, settingsId):
    account = request.user
    print(settingsId)
    try:
        settings = GroupSettings.objects.get(id=settingsId)
    except GroupSettings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if settings.group.owner != account:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return Response(GroupSettingsSerializer(settings).data)
    if request.method == 'PUT':
        if settings.group.owner != account:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = GroupSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_group_settings(request):
    if request.method == 'POST':
        serializer = GroupSettingsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
