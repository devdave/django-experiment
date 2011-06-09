from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=75)
    
class Comment(models.Model):
    title           = models.CharField(max_length=120)
    date_created    = models.DateTimeField("date created")
    src_email       = models.CharField(max_length=150)
    body            = models.TextField()
    #Should default to false, not visible
    visible         = models.BooleanField(default=False)
    
class Post(models.Model):
    title           = models.CharField(max_length=120)
    date_created    = models.DateTimeField("date created")
    date_modified   = models.DateTimeField("date modified")
    author          = models.ForeignKey(Author)
    body            = models.TextField()
    published       = models.BooleanField(default=False)
