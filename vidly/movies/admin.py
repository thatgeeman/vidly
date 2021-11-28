from django.contrib import admin
from django.db.models import fields
from .models import Movie, Genre

# modify the Genre class here
# style guide: Class+admin
class GenreAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin): 
    # can select fields # fields = ('name')
    list_display = ('id', 'title', 'release_year', 'stock')
    exclude = ['date_created']



# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)