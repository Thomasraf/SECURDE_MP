from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    year_of_pub = models.IntegerField()
    ISBN = models.CharField(max_length=17)
    dewey_call = models.CharField(max_length=3)
    reserved = models.BooleanField()
    reviews = models.TextField() #needs to be changed
    
    def __str__(self):
        return self.title
    