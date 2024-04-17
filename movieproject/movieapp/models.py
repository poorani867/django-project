from django.db import models


# Create your models here.
class Movie(models.Model):
    MovieName = models.CharField(max_length=50)
    MovieDirector = models.CharField(max_length=50)
    Language = models.CharField(max_length=50)
    Budget = models.IntegerField()
