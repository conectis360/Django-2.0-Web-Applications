from django.shortcuts import render
from django.views.generic import ( 
        ListView, DetailView,
)
from core.models import Movie

class MovieDetail(DetailView):
    model = Movie
    
class MovieList(ListView): #ListView uses the 'model' to lookup for objects on our database.
    model = Movie
    
    
