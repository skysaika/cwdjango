from django.contrib import admin

from mailing.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Зарегистрировала модель клиента"""
    list_display = ('email', 'first_name', 'last_name', 'comment')

