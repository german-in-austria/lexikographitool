from rest_framework import mixins
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status


from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import RegistrationSerializer, UserSerializer, UserNameSerializer
from .models import Account



@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfully registered a new user."
        data['email'] = account.email
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data)
    else:
        data = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes([IsAuthenticated, ])
def get_user_from_token(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticated, ])
def get_usernames_startwith(request,username):
    user = Account.objects.filter(username__istartswith=username)
    serializer = UserNameSerializer(user, many=True)
    return Response(serializer.data)

