from django.db import models

# Create your models here.
from django.forms import forms,ModelChoiceField


class User(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False,primary_key=True)
    password = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    mobileno = models.BigIntegerField(unique=True, blank=False)
    age=models.IntegerField(blank=False)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = "user_table"

class Category(models.Model):
    category=models.CharField(max_length=10,blank=False)

    class Meta:
        db_table="category_table"

    def __str__(self):
        return self.category



class Movie(models.Model):
    movie_name=models.CharField(max_length=30,blank=False)
    hero=models.CharField(max_length=30,blank=True)
    heroine=models.CharField(max_length=30,blank=True)
    Director=models.CharField(max_length=30,blank=False)
    Release_year=models.CharField(max_length=30,blank=False)
    Age=models.IntegerField(blank=False)
    Rating=models.DecimalField(max_digits = 3,decimal_places = 2)
    Duration=models.CharField(max_length=10,blank=False)
    Genre= models.ForeignKey(Category, on_delete=models.CASCADE,blank=False,default=None)
    Genre_name=models.CharField(max_length=30,blank=False,default=None)
    Description=models.CharField(max_length=500,blank=False)
    picture=models.ImageField(upload_to="picture/",max_length=255,blank=True)

    class Meta:
        db_table="movie_table"

    def __str__(self):
        return self.movie_name

class SearchHistory(models.Model):
    username=models.CharField(max_length=30,blank=False)
    movie_name = models.CharField(max_length=30, blank=False)
    hero = models.CharField(max_length=30, blank=True)
    heroine = models.CharField(max_length=30, blank=True)
    Director = models.CharField(max_length=30, blank=False)
    Genre_name=models.CharField(max_length=30,blank=False,default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="history_table"


