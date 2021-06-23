from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
def index(request):
    return HttpResponse(f'contact')

class BooksListView(ListView):
    model = Books
    paginate_by = 2

    