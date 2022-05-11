from django.contrib import admin

from user.models import User
from stocks.models import StockSymbol, Quote

admin.site.register(User)
admin.site.register(StockSymbol)
admin.site.register(Quote)
