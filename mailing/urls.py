from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import IndexView, contact, ClientCreateView, ClientListView, ClientDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # главная страница

    path('create_client/', ClientCreateView.as_view(), name='create_client'),  # создание клиента
    path('clients/', ClientListView.as_view(), name='clients'),  # список клиентов
    path('client_view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),  # просмотр клиента


    path('contact/', contact, name='contact'),  # путь до страницы контактов FBV
]
