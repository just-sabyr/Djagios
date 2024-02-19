from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from data_collector.models import DataPoint


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('node_name', type=str) # require and parse the argument
        parser.add_argument('data_type', type=str)
        parser.add_argument('data_value', type=float)

    def handle(self, *args, **options):
        node_name = options['node_name']
        data_type = options['data_type']
        data_value = options['data_value']

        new_data_point = DataPoint(node_name=node_name, data_type=data_type, data_value=data_value)
        new_data_point.save()

        print('All data points:')
        print(DataPoint.objects.all())