from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')