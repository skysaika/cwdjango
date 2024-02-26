from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import IndexView, contact

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # главная страница
    path('contact/', contact, name='contact'),  # путь до страницы контактов FBV
]
