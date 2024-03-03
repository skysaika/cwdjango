from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

import mailing
from mailing.forms import ClientForm
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
    form_class = ClientForm  # форма для создания клиента
    template_name = 'mailing/client_form.html'
    extra_context = {
        'title': 'Создание клиента'
    }
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    """Редактирование клиента"""
    model = Client
    form_class = ClientForm  # форма для редактирования клиента
    template_name = 'mailing/client_form.html'
    extra_context = {
        'title': 'Редактирование клиента'
    }
    success_url = reverse_lazy('mailing:client_list')


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
    fields = '__all__'
    extra_context = {
        'title': 'Просмотр клиента'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





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
