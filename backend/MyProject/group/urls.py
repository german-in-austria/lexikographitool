from django.urls import path, include
from .views import *

app_name = "group"
urlpatterns = [
    path('group/', create_group, name='group'),
    path('groups/', get_own_groups, name='get_own_groups'),
    path('group/<int:groupId>/<username>/', add_or_remove_user, name='addOrRemoveUser'),
    path('group/<int:groupId>/', get_group_by_id, name='getGroupById'),
]