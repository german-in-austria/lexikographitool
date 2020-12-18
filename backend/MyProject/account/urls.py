from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

app_name = "account"
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('me/', get_user_from_token, name='me'),
    path('users/<username>/', get_usernames_startwith, name='getusers'),
]