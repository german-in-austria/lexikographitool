from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('origin/<str:zip_or_place>/', origin_by_zip_or_place),
    path('home/', get_home),
    path('location/', create_address),
    path('locations/', get_locations),
    path('cards/', card_list),
    path('own_cards/', card_own),
    path('lexeme/', create_lexeme),
    path('dialect/', create_dialect),
    path('etymology/', create_etymology),
    path('pronunciation/', create_pronunciation),
    path('example/', create_example),
    path('lexemes_simple/', LexemeSimpleListView.as_view(), name='lexemes_simple'),
    path('varieties/<search>/', get_variety_list, name='dialects'),
    path('categories/', CategoryListView.as_view(), name='categoriesc'),
    path('lexeme_by_word/<word>/', lexeme_first_by_word),
    path('category/<pk>/', create_category),
    path('lexeme/<lexemeId>/', get_lexeme),
    path('lexemes/', LexemeView.as_view()),
    path('lexeme/like/<lexemeId>/', like_lexeme),
    path('lexemes/random/',get_random_lexemes),
    path('lexemes/popular/',get_most_popular),
    path('lexemes/discussed/',get_most_discussed),
    path('lexemes/similar/<lexemeId>/',get_similar_lexemes),
    path('report/lexeme/<lexemeId>/', report_lexeme),
    path('reports/lexeme/', ReportView.as_view()),
    path('report/lexeme/deactivate/<reportId>/', deactive_report),

]