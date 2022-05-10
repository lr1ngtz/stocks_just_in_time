from django.urls import path

from user.views import UserCreate

urlpatterns = [
    path("sign-up/", UserCreate.as_view()),
]
