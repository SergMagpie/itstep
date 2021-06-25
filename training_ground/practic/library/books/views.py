from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


def index(request):
    return HttpResponse(f'contact')


class BooksListView(ListView):
    model = Books
    paginate_by = 5
    # def get_queryset(self):

    #     return super().get_queryset()
    queryset = (Books.objects
                .values('author__name')
                .annotate(dcount=Count('title'))
                .order_by('-dcount')[:1]
                )
    # Books.objects.filter(year_of_publication__gte=2020)

# Books.objects.values('author__name').annotate(dcount=Count('pk'))
# all().group_by('author')
# filter(author__gte=F())
