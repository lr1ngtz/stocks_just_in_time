from django.core.management.base import BaseCommand

from stocks.tasks import create_or_update_stock_symbol_task


class Command(BaseCommand):
    help = "Create or update stocks"

    def handle(self, *args, **options):
        create_or_update_stock_symbol_task.delay()
