from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def main_menu(active, request=None):
    menu_list = [
        {"title": "Home", "url_name": "/", "class": ""},
        {"title": "First task", "url_name": "first-task", "class": ""},
        {"title": "Words", "url_name": "words", "class": ""},
        {"title": "Add word", "url_name": "add-word", "class": ""},
        {"title": "New user", "url_name": "new-user", "class": ""},
        {"title": "Login", "url_name": "login", "class": ""},
    ]
    for item in menu_list:
        if item["title"] == active:
            item["class"] = "active"
        else:
            item["class"] = ""
    if request and request.user.is_authenticated:
        menu_list[5] = {'title': "Logout", "url_name": "logout", "class": ""}
    else:
        menu_list.pop(3)
    return menu_list


def index(request):
    context = {
        'title': 'lesson 43',
        'main_menu': main_menu('Home', request),
    }
    print(request.user)
    return render(request, 'wlearn/home.html', context=context)

# def new_user(request):
#     return HttpResponse("The new_user page")


# def words(request):
#     return HttpResponse("The words page")


class ShowWords(ListView):
    model = Words
    template_name = 'wlearn/words.html'
    context_object_name = 'words'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Words")
        c_def = {
            'title': 'Words',
            'main_menu': main_menu('Words', self.request),

        }
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Words.objects.all()


# def login(request):
#     return HttpResponse("The login page")

@login_required(login_url='login')
def add_word(request):
    return HttpResponse("The add_word page")


def first_task(request):
    rez, numbers, mission = None, [], None
    if request.method == 'POST':
        numbers = [
            int(request.POST.get('first_number') or 0),
            int(request.POST.get('second_number') or 0),
            int(request.POST.get('third_number') or 0),
        ]
        mission = request.POST.get('mission')
        missions = {
            'minimum': min,
            'maximum': max,
            'mean': lambda x: sum(x) / len(x)
        }
        if mission in missions:
            rez = missions[mission](numbers)
    context = {
        'title': 'First task with lesson 43',
        'rez': rez,
        'numbers': numbers,
        'mission': mission,
        'main_menu': main_menu('First task', request),

    }
    return render(request, 'wlearn/first_task.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'wlearn/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.get_user_context(title='Registration')
        c_def = {
            'title': 'Registration',
            'main_menu': main_menu('New user', self.request),
        }
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('words')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'wlearn/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.get_user_context(title='Registration')
        c_def = {
            'title': 'Login',
            'main_menu': main_menu('Login', self.request),
        }
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('words')


def logout_user(request):
    logout(request)
    return redirect('words')
