from core import celery_app

from stocks.services.stock_symbol import create_or_update_stock_symbol
from stocks.services.quote import create_quote


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        20,
        create_quote_task.s("AAPL"),
        name="scan for expired accounts every 4 hours",
    )


@celery_app.task
def create_or_update_stock_symbol_task():
    create_or_update_stock_symbol()


@celery_app.task
def create_quote_task(quote):
    create_quote(quote)
