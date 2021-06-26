from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    path("add-actor/", ActorCreateView.as_view(), name='add_actor'),
    path("add-genre/", GenreCreateView.as_view(), name='add_genre'),
    path("add-movie/", MovieCreateView.as_view(), name='add_movie'),
    path("movies/", MoviesListView.as_view(), name='movies'),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name='movies_numb'),
    path("movies/<int:pk>/change/", MovieUpdateView.as_view(), name='movie_change'),
    path("", IndexTemplateView.as_view(), name='home'),
]
