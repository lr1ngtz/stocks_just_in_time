from celery import shared_task

from stocks.services.stock_symbol import create_or_update_stock_symbol


@shared_task
def create_or_update_stock_symbol_task():
    create_or_update_stock_symbol()
