# from django.core.mail import send_mail
# from datetime import datetime
# from mailing.models import MailingList
#
#
# def send_mailings():
#     """Функция для отправки писем с учетом всех условий и проверок"""
#
#     # Получаем все рассылки, удовлетворяющие условиям начала и окончания рассылки
#     mailings = MailingList.objects.filter(mail_start__lte=datetime.now().date(), mail_end__gte=datetime.now().date(),
#                                           mail_status='Создана')
#
#     for mailing in mailings:
#         if mailing.mail_period == 'Ежедневно':
#             recipients = mailing.recipient.all()
#             if recipients:
#                 send_mail(recipients, mailing.message.subject, mailing.message.body)
#                 print(f"Sent daily emails for {mailing} to {len(recipients)} recipients.")
#             else:
#                 print(f"No recipients found for {mailing}.")
#
#         elif mailing.mail_period == 'Еженедельно' and datetime.now().weekday() == 6:
#             recipients = mailing.recipient.all()
#             if recipients:
#                 send_mail(recipients, mailing.message.subject, mailing.message.body)
#                 print(f"Sent weekly emails for {mailing} to {len(recipients)} recipients.")
#             else:
#                 print(f"No recipients found for {mailing}.")
#
#         elif mailing.mail_period == 'Ежемесячно' and datetime.now().day == 1:
#             recipients = mailing.recipient.all()
#             if recipients:
#                 send_mail(recipients, mailing.message.subject, mailing.message.body)
#                 print(f"Sent monthly emails for {mailing} to {len(recipients)} recipients.")
#             else:
#                 print(f"No recipients found for {mailing}.")
#
#         else:
#             print(f"No mails to be sent for {mailing}.")
from datetime import datetime

from mailing.models import MailingList, MailingLog


# from django.core.mail import send_mail
# from datetime import datetime
# from mailing.models import MailingList
#
#
# def my_func_daily():
#     """Функция для отправки писем с учетом всех условий"""
#     # Получаем все рассылки, удовлетворяющие условиям начала и окончания рассылки
#     mailings = MailingList.objects.filter(mail_start__lte=datetime.now().date(), mail_end__gte=datetime.now().date(),
#                                           mail_status='Создана')
#
#     for mailing in mailings:
#         if mailing.mail_period == 'Ежедневно':
#             send_mail(mailing.recipient.all(), mailing.message.subject, mailing.message.body)
#         elif mailing.mail_period == 'Еженедельно':
#             if datetime.now().weekday() == 6:  # Проверка, что сегодня воскресенье
#                 send_mail(mailing.recipient.all(), mailing.message.subject, mailing.message.body)
#         elif mailing.mail_period == 'Ежемесячно':
#             if datetime.now().day == 1:  # Проверка, что сегодня первое число месяца
#                 send_mail(mailing.recipient.all(), mailing.message.subject, mailing.message.body)

# def my_func_daily():
#     print('daily')
#
#
# def my_func_weekly():
#     print('weekly')
#
#
# def my_func_monthly():
#     print('monthly')
# from datetime import datetime
# from mailing.models import MailingList, MailingLog
#
# def send_daily_mail():
#     """Функция для ежедневной отправки писем"""
#     # Получаем рассылки для текущей даты и статусом "Создана"
#     daily_mailings = MailingList.objects.filter(
#         mail_start__lte=datetime.now().date(),
#         mail_end__gte=datetime.now().date(),
#         mail_period='Ежедневно',
#         mail_status='Создана'
#     )
#
#     for mailing in daily_mailings:
#         recipients = mailing.recipient.all()
#         for recipient in recipients:
#     # Отправка письма recipient.email, mailing.message.subject, mailing.message.body
#
#         # Логирование попытки отправки
#         MailingLog.objects.create(
#             last_attempt_time=datetime.now(),
#             attempt_status='SUCCESS',
#             server_response='Письмо успешно отправлено',
#             mailing=mailing
#         )
#
# def send_weekly_mail():
#     """Функция для еженедельной отправки писем"""
#     # Получаем рассылки для текущей даты и статусом "Создана"
#     weekly_mailings = MailingList.objects.filter(
#         mail_start__lte=datetime.now().date(),
#         mail_end__gte=datetime.now().date(),
#         mail_period='Еженедельно',
#         mail_status='Создана'
#     )
#
#     for mailing in weekly_mailings:
#         if datetime.now().weekday() == 6:  # Проверка, что сегодня воскресенье
#             recipients = mailing.recipient.all()
#             for recipient in recipients:
#         # Отправка письма recipient.email, mailing.message.subject, mailing.message.body
#
#             # Логирование попытки отправки
#             MailingLog.objects.create(
#                 last_attempt_time=datetime.now(),
#                 attempt_status='SUCCESS',
#                 server_response='Письмо успешно отправлено',
#                 mailing=mailing
#         )
#
# def send_monthly_mail():
#     """Функция для ежемесячной отправки писем"""
#     # Получаем рассылки для текущей даты и статусом "Создана"
#     monthly_mailings = MailingList.objects.filter(
#         mail_start__lte=datetime.now().date(),
#         mail_end__gte=datetime.now().date(),
#         mail_period='Ежемесячно',
#         mail_status='Создана'
#     )
#
#     for mailing in monthly_mailings:
#         if datetime.now().day == 1:  # Проверка, что сегодня первое число месяца
#             recipients = mailing.recipient.all()
#             for recipient in recipients:
#         # Отправка письма recipient.email, mailing.message.subject, mailing.message.body
#
#             # Логирование попытки отправки
#             MailingLog.objects.create(
#                 last_attempt_time=datetime.now(),
#                 attempt_status='SUCCESS',
#                 server_response='Письмо успешно отправлено',
#                 mailing=mailing
#             )
# После создания новой рассылки,
# если текущее время больше времени начала и меньше времени окончания,
# то должны быть выбраны из справочника все клиенты,
# которые указаны в настройках рассылки,
# и запущена отправка для всех этих клиентов.
def send_newletter():
    """
    После создания новой рассылки,
    если текущее время больше времени начала и меньше времени окончания,
    то должны быть выбраны из справочника все клиенты,
    которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
    """
    # Получаем все рассылки, удовлетворяющие условиям начала и окончания рассылки
    mailings = MailingList.objects.filter(
        mail_start__lte=datetime.now().date(),
        mail_end__gte=datetime.now().date(),
        mail_status='Создана')

    for mailing in mailings:
        # Выбираем все клиентов, удовлетворяющие условиям рассылки
        recipients = mailing.recipient.all()
        for recipient in recipients:
            # Отправка письма recipient.email, mailing.message.subject, mailing.message.body
            # Логирование попытки отправки
            MailingLog.objects.create(
                last_attempt_time=datetime.now(),
                attempt_status='SUCCESS',
                server_response='Письмо успешно отправлено',
                mailing=mailing
            )

