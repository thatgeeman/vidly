from datetime import time
from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):  # makes an API
    name = models.CharField(max_length=255) 
    # if we use this it will show as Genre object in the admin panel.

    def __str__(self) -> str:
        """override the charfield method to actually a string"""
        return self.name


class Movie(models.Model):  # makes an API
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now) 
    # passing the reference to method (updates to timezone of user)
    
    def __str__(self) -> str:
        """override the charfield method to actually a string"""
        return self.title