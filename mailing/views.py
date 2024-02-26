from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Представление главной страницы."""
    template_name = 'mailing/index.html'


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
