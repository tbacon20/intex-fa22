from operator import index
from django.urls import path
from .views import signUpPageView

urlpatterns = [
    path("", signUpPageView, name="index"),
]