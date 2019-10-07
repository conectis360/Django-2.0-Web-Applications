from django.shortcuts import render
from django.views.generic import ( 
        ListView, DetailView,
)
from core.models import Movie

class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons()
    )
    
class MovieList(ListView): #ListView uses the 'model' to lookup for objects on our database.
    model = Movie
    
class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()
    
    
    
