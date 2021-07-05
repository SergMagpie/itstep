from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('welcome-mail/', MailTemplateView.as_view(), name='welcome_mail'),
]