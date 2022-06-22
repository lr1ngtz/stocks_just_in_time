from django.db import models

from core.models import BaseModel
from stocks.models import StockSymbol
from user.models import User


class Portfolio(BaseModel):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbols = models.ManyToManyField(StockSymbol)
