from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
main_menu = [
    {"title": "Home", "url_name": "/"},
    {"title": "Words", "url_name": "words"},
    {"title": "New user", "url_name": "new-user"},
    {"title": "Login", "url_name": "login"},
    {"title": "Add word", "url_name": "add-word"},
    {"title": "First task", "url_name": "first-task"},
]


def index(request):
    string = ''
    for i in main_menu:
        string += f"<a href='{i['url_name']}'>{i['title']}</a><br>"
    return HttpResponse(f"<h1>The index page</h1>{string}")

def new_user(request):
    return HttpResponse("The new_user page")

def words(request):
    return HttpResponse("The words page")

def login(request):
    return HttpResponse("The login page")

def add_word(request):
    return HttpResponse("The add_word page")

def first_task(request):
    return HttpResponse("The first_task page")

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'wlearn/register.html'
    success_url = reverse_lasy('login')
