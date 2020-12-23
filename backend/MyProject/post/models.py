from django.conf import settings
from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    date_created = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
