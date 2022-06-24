import factory

from portfolio.models import Portfolio
from stocks.models import StockSymbol
from user.models import User


class StockSymbolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockSymbol

    symbol = factory.Faker("word")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("email")
    phone = factory.Faker("email")


class PortfolioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Portfolio

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("word")

    # @factory.post_generation
    # def stock_symbols(self, create, extracted, **kwargs):
    #     if not create:
    #         return

    #     if extracted:
    #         for group in extracted:
    #             self.stock_symbols.add(group)
