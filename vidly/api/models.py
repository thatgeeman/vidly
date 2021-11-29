from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        # tastypie looks for Meta inner class
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
        