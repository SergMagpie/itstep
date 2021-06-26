from django.urls import path
from wlearn.views import *

urlpatterns = [
    path("", index, name='home'),
    path("words/", ShowWords.as_view(), name='words'),
    path("new-user/", RegisterUser.as_view(), name='new_user'),
    path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("add-word/", AddWord.as_view(), name='add_word'),
    path("change-word/<int:pk>/", ChangeWord.as_view(), name='change_word'),
    path("first-task/", first_task, name='first_task'),
]
