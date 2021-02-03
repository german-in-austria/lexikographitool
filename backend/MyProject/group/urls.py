from django.urls import path, include
from .views import *

app_name = "group"
urlpatterns = [
    path('group/settings/', create_group_settings, name='settings'),
    path('group/settings/<settingsId>/', get_update_group_settings, name='settings'),

    path('group/', create_group, name='group'),
    path('groups/', get_own_groups, name='get_own_groups'),
    path('group/<int:groupId>/<username>/', add_or_remove_user, name='addOrRemoveUser'),
    path('group/<int:groupId>/', get_update_group, name='getGroupById'),

    path('invite/<int:groupId>/', get_invite_link, name='getInviteLink'),
    path('join/<int:groupId>/<str:hash>/', join_group, name='joinGroup'),
    path('groupname/<int:groupId>/<str:hash>/', get_group_name_by_invite, name='getNameByInvite'),
]