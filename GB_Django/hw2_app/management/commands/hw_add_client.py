from django.core.management.base import BaseCommand
from hw2_app.models import Client
import names


class Command(BaseCommand):
    help = 'Generate fake clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Jhon{i}',
                            email=f'a{i}b@mail.ru',
                            phone_number=f'{i * 3945512}',
                            address=f'some adress house.{i}',
                            reg_date=f'2002-05-12', )
            client.save()
