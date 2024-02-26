from django.core.management import BaseCommand

from mailing.models import Client


class Command(BaseCommand):
    help = 'Fill database with test data'

    def handle(self, *args, **options):
        client_list = [
            {
                'email': 'pJ8ZK@example.com',
                'first_name': 'Test',
                'last_name': 'Testov',
                'comment': '# test'
            },
            {
                'email': 'pJ8ZK@example.com',
                'first_name': 'Testina',
                'last_name': 'Testova',
                'comment': '#2'
            },
            {
                'email': 'pJ8ZK@example.com',
                'first_name': 'Oleg',
                'last_name': 'Maslov',
                'comment': None
            },
        ]

        clients_for_create = []
        for clients_item in client_list:
            clients_for_create.append(
                Client(**clients_item)
            )

        Client.objects.bulk_create(clients_for_create)  # пакетное создание
