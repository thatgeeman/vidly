from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
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

def detail(request, movie_id):
    """ can also use try except or get_object_or_404
    try:
        movie = Movie.objects.get(id=movie_id) # pk: primary key
        # calls an sql like select * from movie
        # similary can filter, get, delete objects too
        # output = ', '.join([m.title for m in movies]) # get all titles from the Movie object
        # return HttpResponse(output)
        return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        return Http404
    """
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})