from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # only passing the reference to function
]