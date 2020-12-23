from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('origin/<str:zip_or_place>/', origin_by_zip_or_place),
    path('cards/', card_list),
    path('own_cards/', card_own),
    path('lexeme/', create_lexeme),
    path('dialect/', create_dialect),
    path('etymology/', create_etymology),
    path('pronunciation/', create_pronunciation),
    path('example/', create_example),
    path('lexemes_simple/', LexemeListView.as_view(), name='lexemes_simple'),
    path('dialects/', DialectListView.as_view(), name='dialects'),
    path('categories/', CategoryListView.as_view(), name='categoriesc'),
    path('lexeme_by_word/<word>/', lexeme_first_by_word),
    path('category/<pk>/', create_category),
    path('lexeme/<lexemeId>/', get_lexeme),

]