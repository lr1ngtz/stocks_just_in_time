from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import Response

from portfolio.serializers import PortfolioSerializer
from portfolio.models import Portfolio
from portfolio.services.portfolio import create_stock_symbols
from stocks.serializers import StockSymbolSerializer, CreateStockSymbolSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    @action(methods=["GET", "POST"], detail=True)
    def stock_symbols(self, request, pk=None):
        portfolio = get_object_or_404(Portfolio, pk=pk)
        if request.method == "POST":
            serializer = CreateStockSymbolSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            create_stock_symbols(portfolio, serializer)
        stock_symbols = portfolio.stock_symbols.all()
        serializer = StockSymbolSerializer(stock_symbols, many=True)
        return Response(serializer.data)
