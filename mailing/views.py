from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from mailing.models import MailingList, Client


class IndexView(TemplateView):
    """Представление главной страницы."""
    template_name = 'mailing/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': MailingList.objects.all()
    }


class ClientCreateView(CreateView):
    """Создание клиента"""
    model = Client
    template_name = 'mailing/client_form.html'
    fields = ['email', 'first_name', 'last_name', 'comment']
    extra_context = {
        'title': 'Создание клиента'
    }


class ClientListView(ListView):
    """Просмотр списка клиентов"""
    model = Client
    template_name = 'mailing/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientDetailView(TemplateView):
    """Просмотр одного клиента"""
    model = Client
    template_name = 'mailing/client_detail.html'
    extra_context = {
        'title': 'Просмотр клиента'
    }





def contact(request):
    """Контроллер страницы контактов на FBV"""
    # метод POST - получение данных, не забудь вернуть context
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'name:{name}, email:{email}, {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mailing/contact.html', context)
