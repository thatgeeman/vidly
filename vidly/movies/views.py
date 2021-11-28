from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre
# Create your views here.

def index(request):
    movies = Movie.objects.all() 
    # calls an sql like select * from movie
    # similary can filter, get, delete objects too
    # output = ', '.join([m.title for m in movies]) # get all titles from the Movie object
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

