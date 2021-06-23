from django.urls import path

from .views import *

urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
]