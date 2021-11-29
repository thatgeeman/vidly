from django.urls import path
from . import views

app_name = 'movies' # django keyword

urlpatterns = [
    path('', views.index, name='index'), # only passing the reference to function
    path('<int:movie_id>', views.detail, name='detail'), # int: is a type converter
]