from django.contrib import admin

from mailing.models import Client, MailingMessage, MailingList, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Админка модели клиента"""
    list_display = ('email', 'first_name', 'last_name', 'comment',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    """Админка модели сообщения"""
    list_display = ('subject', 'body',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    """Админка модели рассылки"""
    list_display = ('mail_start', 'mail_end', 'mail_period', 'mail_status',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    """Админка модели логов рассылок"""
    list_display = ('last_attempt_time', 'attempt_status', 'server_response',)
