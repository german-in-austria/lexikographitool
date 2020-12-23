from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('post/', create_post),
    path('post/<int:id>/', get_post_by_id),
    path('posts/', get_posts),

]