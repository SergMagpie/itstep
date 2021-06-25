from django.urls import path
from wlearn.views import *

urlpatterns = [
    path("", index, name='home'),
    path("words", words, name='words'),
    path("new-user", RegisterUser.as_view(), name='new_user'),
    path("login", LoginUser.as_view(), name='login'),
    path("add-word", add_word, name='add_word'),
    path("first-task", first_task, name='first_task'),
]
