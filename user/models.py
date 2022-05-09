from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        BROKER = "BR", _("Broker")
        TRADER = "TR", _("Trader")
        MARKETING = "MR", _("Marketing")
        INDIVIDUAL = "IN", _("Individual")
        FINANCE = "FI", _("Finance")
        DEVELOPER = "DE", _("Developer")
        DATA_SCIENTIST = "DS", _("Data Scientist")

    class Country(models.TextChoices):
        US = "US"
        GERMANY = "DE"
        JAPAN = "JP"
        BELARUS = "BY"
        CANADA = "CA"
        UK = "UK"
        POLAND = "PL"
        DENMARK = "DK"

    phone = models.CharField(max_length=30, unique=True, verbose_name="Phone")
    country = models.CharField(
        max_length=9, choices=Country.choices, verbose_name="Country"
    )
    company = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Company"
    )
    role = models.CharField(max_length=9, choices=Role.choices, verbose_name="Role")
    bio = models.TextField(null=True, blank=True)
