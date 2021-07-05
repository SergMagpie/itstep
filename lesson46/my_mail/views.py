from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'my_mail/index.html'


class MailTemplateView(TemplateView):
    template_name = 'my_mail/my_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'About the site',
        }
        return dict(list(context.items()) + list(insert_def.items()))

    def post(self, request, *args, **kwargs):
        if request.POST:
            fio = request.POST['fio']
            email = request.POST['email']
            message = Mail(
                from_email='sergmagpie@gmail.com',
                to_emails=email,
                subject='Вітання!',
                html_content=f'<strong>Вітання від {fio}</strong>')
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print('response.status_code', response.status_code)
            print('response.body', response.body)
            print('response.headers', response.headers)
        except Exception as e:
            print('e', e)
        return HttpResponseRedirect('/')
