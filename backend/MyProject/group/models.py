from django.conf import settings
from django.db import models

from account.models import Account

class GroupSettings(models.Model):
    members_createCollection = models.BooleanField(default=False)
    members_add_remove_lexemes = models.BooleanField(default=False)

    public_createCollection = models.BooleanField(default=False)
    public_add_remove_lexemes = models.BooleanField(default=True)

    need_password = models.BooleanField(default=False)
    join_password = models.CharField(max_length=100, null=True)

    public = models.BooleanField(default=False)


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(Account, related_name='groupsOwned', on_delete=models.CASCADE)
    members = models.ManyToManyField(Account, related_name='groups')
    organization = models.CharField(max_length=100,null=True)
    settings = models.OneToOneField(GroupSettings, related_name='group', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + str(self.id)
