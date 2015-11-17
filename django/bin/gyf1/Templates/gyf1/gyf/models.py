#-*- coding: cp936 -*-
from django.db import models
from django.contrib.auth.models import User

class Authors(models.Model):
    AuthorID = models.CharField(max_length=30)
    Name = models.CharField(max_length = 15)
    Age = models.CharField(max_length=30)
    Country = models.CharField(max_length=20)
    
class Books(models.Model):
    ISBN = models.CharField(max_length=30)
    Title = models.CharField(max_length = 15)
    AuthorID = models.ForeignKey(Authors)
    Publisher = models.CharField(max_length = 20)
    PublishDate = models.CharField(max_length = 18)
    Price = models.CharField(max_length=11)
    
