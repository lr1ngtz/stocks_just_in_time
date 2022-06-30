from django.db import models

from core.models import BaseModel


class StockSymbol(BaseModel):
    description = models.CharField(max_length=255)
    display_symbol = models.CharField(max_length=32)
    figi = models.CharField(max_length=64)
    isin = models.CharField(max_length=32, null=True)
    mic = models.CharField(max_length=32)
    share_class_figi = models.CharField(max_length=64)
    symbol = models.CharField(max_length=32)
    symbol2 = models.CharField(max_length=32)
    type = models.CharField(max_length=32)

    def __str__(self):
        return f"Stock Symbol: {self.symbol}"


class Quote(BaseModel):
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    percent_change = models.DecimalField(max_digits=8, decimal_places=5)
    high_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    low_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    open_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    previous_close_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()
    stock_symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
