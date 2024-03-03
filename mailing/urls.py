from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import IndexView, contact, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # главная страница

    path('create_client/', ClientCreateView.as_view(), name='create_client'),  # создание клиента
    path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),  # редактирование клиента
    path('client_list/', ClientListView.as_view(), name='client_list'),  # список клиентов
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),  # просмотр клиента


    path('contact/', contact, name='contact'),  # путь до страницы контактов FBV
]
