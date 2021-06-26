from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from .models import Movie, Genre
from datetime import date
from .forms import *
from django.urls import reverse_lazy
from actors.models import Actor
from django.views.generic import CreateView
from django.utils import timezone

# Create your views here.


class MovieCreateView(CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/create_movie_form.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        movie = form.save(commit=False)
        movie.created_at = timezone.now()
        movie.save()
        self.object = form.save_m2m()
        return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/change_movie_form.html'


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movies.html'



class IndexTemplateView(TemplateView):
    template_name = 'movies/index.html'



class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/moves_numb.html'
    context_object_name = 'move'


def add_actor(request):
    if request.method == "POST":
        form = AddActorForm(request.POST)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return HttpResponse("<h3>Actor was saved</h3>")
        print(form.errors)
        return HttpResponse("<h3>Error</h3>")
    else:
        form = AddActorForm()
        context = {'form': form}
        return render(request, 'movies/create_actor_form.html', context)


class ActorCreateView(CreateView):
    model = Actor
    form_class = AddActorForm
    template_name = 'movies/create_actor_form.html'
    success_url = reverse_lazy('movies')

class GenreCreateView(CreateView):
    model = Genre
    form_class = AddGenreForm
    template_name = 'movies/create_genre_form.html'
    success_url = reverse_lazy('movies')

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     movie = form.save(commit=False)
    #     movie.created_at = timezone.now()
    #     movie.save()
    #     self.object = form.save_m2m()
    #     return super().form_valid(form)

# def add_genre(request):
#     if request.method == "POST":
#         form = AddGenreForm(request.POST)
#         if form.is_valid():
#             genre = form.save(commit=False)
#             genre.save()
#             return HttpResponse("<h3>Genre was saved</h3>")
#         print(form.errors)
#         return HttpResponse("<h3>Error</h3>")
#     else:
#         form = AddGenreForm()
#         context = {'form': form}
#         return render(request, 'movies/create_genre_form.html', context)
