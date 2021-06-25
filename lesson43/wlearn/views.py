from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

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
    context = {
        'title': 'lesson 43',
     }
    return render(request, 'wlearn/home.html', context=context)

# def new_user(request):
#     return HttpResponse("The new_user page")


def words(request):
    return HttpResponse("The words page")

# def login(request):
#     return HttpResponse("The login page")


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
    }
    return render(request, 'wlearn/first_task.html', context=context)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'wlearn/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.get_user_context(title='Registration')
        c_def = {'title': 'Registration'}
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'wlearn/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.get_user_context(title='Registration')
        c_def = {'title': 'Login'}
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('words')
