from django.conf import settings
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
CHOICE_KIND = (
    ('N', 'noun'),
    ('V', 'verb'),
    ('Aj', 'adjective'),
    ('Av', 'adverb'),
    ('P', 'phrase'))


class Address(models.Model):
    country_code = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True,blank=True)
    place = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    state_code = models.CharField(max_length=100, null=True,blank=True)
    province = models.CharField(max_length=100, null=True,blank=True)
    province_code = models.CharField(max_length=100, null=True,blank=True)
    community = models.CharField(max_length=100, null=True,blank=True)
    community_code = models.CharField(max_length=100, null=True,blank=True)
    latitude = models.CharField(max_length=100, null=True,blank=True)
    longitude = models.CharField(max_length=100, null=True,blank=True)


class Dialect(models.Model):
    dialect = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.dialect


# Create your models here.
class Lexeme(models.Model):
    word = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True,blank=True)
    kind = models.CharField(max_length=255, choices=CHOICE_KIND)
    dialectWord = models.CharField(max_length=100)
    origin = models.ForeignKey(Address, related_name='dialectWords', on_delete=models.CASCADE)
    dialect = models.ForeignKey(Dialect, related_name='dialectWords', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #def __str__(self):
    #    return self.word



class Category(models.Model):
    category = models.CharField(max_length=100, primary_key=True)
    lexemes = models.ManyToManyField(Lexeme, related_name='categories')


class DialectWord(models.Model):
    word = models.CharField(max_length=100, primary_key=True)

    # lexeme = models.ForeignKey(Lexeme, related_name='dialectWords', on_delete=models.CASCADE)
    # origin = models.ForeignKey(Address, related_name='dialectWords', on_delete=models.CASCADE)
    # dialect = models.ForeignKey(Dialect, related_name='dialectWords', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.word


class Example(models.Model):
    example = models.CharField(max_length=100)
    dialectWord = models.ForeignKey(Lexeme, related_name='examples', on_delete=models.CASCADE)

    def __str__(self):
        return self.example


class Pronunciation(models.Model):
    pronunciation = models.CharField(max_length=100)
    dialectWord = models.ForeignKey(Lexeme, related_name='pronunciations', on_delete=models.CASCADE)

    def __str__(self):
        return self.pronunciation


class Etymology(models.Model):
    etymology = models.CharField(max_length=100)
    dialectWord = models.ForeignKey(Lexeme, related_name='etymologies', on_delete=models.CASCADE)

    def __str__(self):
        return self.etymology


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
