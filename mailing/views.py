from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Представление главной страницы."""
    template_name = 'mailing/index.html'


