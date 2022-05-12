from django.contrib import admin
from django.contrib.admin.decorators import display

from stocks.models import StockSymbol, Quote


@admin.register(StockSymbol)
class StockSymbolAdmin(admin.ModelAdmin):
    list_display = ("symbol", "description")


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("symbol_name", "current_price", "time_stamp")
    list_filter = ("time_stamp",)
    search_fields = ("stock_symbol__symbol",)

    @display(ordering="stock_symbol", description="Symbol")
    def symbol_name(self, obj):
        return obj.stock_symbol.symbol
