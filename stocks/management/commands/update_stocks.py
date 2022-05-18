from django.core.management.base import BaseCommand

from stocks.services.stock_symbol import create_or_update_stock_symbol


class Command(BaseCommand):
    help = "Create or update stocks"

    def handle(self, *args, **options):
        create_or_update_stock_symbol()
