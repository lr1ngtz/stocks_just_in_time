from django.urls import include, path
from rest_framework import routers

from portfolio.views import PortfolioViewSet

router = routers.DefaultRouter()
router.register(r"", PortfolioViewSet, basename="portfolio")


urlpatterns = [
    path("", include(router.urls)),
]
