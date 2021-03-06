from django.core.management.base import BaseCommand

from stocks.tasks import create_quote_task


class Command(BaseCommand):
    help = "Create quote"

    def add_arguments(self, parser):
        parser.add_argument("quote", type=str)

    def handle(self, *args, **options):
        create_quote_task.delay(options["quote"])
