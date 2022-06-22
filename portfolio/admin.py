from django.contrib import admin

from portfolio.models import Portfolio


@admin.register(Portfolio)
class StockSymbolAdmin(admin.ModelAdmin):
    list_display = ("name", "user_id")
