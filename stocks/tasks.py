from celery import shared_task
from core import celery_app

from stocks.services.stock_symbol import create_or_update_stock_symbol
from stocks.services.quote import create_quote


@celery_app.task
def create_or_update_stock_symbol_task():
    create_or_update_stock_symbol()


@celery_app.task
def create_quote_task(quote):
    create_quote(quote)
