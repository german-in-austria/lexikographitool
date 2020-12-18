from django.conf import settings
from django.db import models

from account.models import Account

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(Account, related_name='groupsOwned', on_delete=models.CASCADE)
    members = models.ManyToManyField(Account, related_name='groups')

