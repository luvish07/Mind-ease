from django.urls import path

from . import views


app_name = "wellness"

urlpatterns = [
    path("", views.home, name="home"),
]
