from django.db import models


class StockSymbol(models.Model):
    currency = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    display_symbol = models.CharField(max_length=32)
    figi = models.CharField(max_length=64)
    isin = models.CharField(max_length=32, null=True)
    mic = models.CharField(max_length=32)
    share_class_figi = models.CharField(max_length=64)
    symbol = models.CharField(max_length=32)
    symbol2 = models.CharField(max_length=32)
    type = models.CharField(max_length=32)


class Quote(models.Model):
    c = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Current price"
    )
    d = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Change")
    dp = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Percent change"
    )
    h = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="High price of the day"
    )
    l = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Low price of the day"
    )
    o = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Open price of the day"
    )
    pc = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Previous close price"
    )
    t = models.PositiveIntegerField(verbose_name="Timestamp")
