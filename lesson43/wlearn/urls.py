from django.urls import path
from wlearn.views import *

urlpatterns = [
    path("", index, name='home'),
    path("words", words, name='words'),
    path("new-user", new_user, name='new_user'),
    path("login", login, name='login'),
    path("add-word", add_word, name='add_word'),
    path("first-task", first_task, name='first_task'),
]
