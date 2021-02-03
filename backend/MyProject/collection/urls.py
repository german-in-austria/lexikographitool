from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = "account"
urlpatterns = [
    path('collections/', get_collections),
    path('collectionsbygroups/', get_collections_split_by_group),
    path('collectionsbygroups/<int:lexemeId>/', get_collections_split_by_group_and_lexeme),
    path('collections/owner/', get_collections_by_owner),
    path('collection/', create_collection),
    path('collection/<collectionId>/', get_update_collection),
    path('collection/<collectionId>/<lexemeId>/', add_or_remove_lexeme_to_collection),
    path('favorite/<lexemeId>/', add_or_remove_lexeme_to_favorites),
    path('collection/group/<int:collectionId>/<int:groupId>/', add_group_to_collection),
]