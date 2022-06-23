from django.urls import include, path
from rest_framework import routers

from portfolio.views import PortfolioViewSet

router = routers.DefaultRouter()
router.register(r"", PortfolioViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
