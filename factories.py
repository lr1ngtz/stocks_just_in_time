import factory

from portfolio.models import Portfolio
from stocks.models import StockSymbol
from user.models import User


class StockSymbolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StockSymbol


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
