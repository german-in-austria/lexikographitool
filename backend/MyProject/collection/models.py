from django.conf import settings
from django.db import models

from lexeme.models import Lexeme,Category
from group.models import Group



class Collection(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100, null=True, blank=True)
    lexemes = models.ManyToManyField(Lexeme, related_name='collections')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='collections')
    public = models.fields.BooleanField(default=False)
    organization = models.fields.CharField(max_length=100, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)