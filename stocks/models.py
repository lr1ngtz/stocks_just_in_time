from django.db import models


class StockSymbol(models.Model):
    description = models.CharField(max_length=255)
    display_symbol = models.CharField(max_length=32)
    figi = models.CharField(max_length=64)
    isin = models.CharField(max_length=32, null=True)
    mic = models.CharField(max_length=32)
    share_class_figi = models.CharField(max_length=64)
    symbol = models.CharField(max_length=32)
    symbol2 = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.symbol}"


class Quote(models.Model):
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    percent_change = models.DecimalField(max_digits=10, decimal_places=2)
    high_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    low_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    open_price_of_the_day = models.DecimalField(max_digits=10, decimal_places=2)
    previous_close_price = models.DecimalField(max_digits=10, decimal_places=2)
    time_stamp = models.DateTimeField()
    stock_symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        symbol = self.stock_symbol.symbol
        time_stamp = self.time_stamp.strftime("%d-%m-%Y %H:%M:%S")

        return f"{symbol}, {self.current_price}, {time_stamp}"
