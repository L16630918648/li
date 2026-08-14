from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.index, name="index"),
    path("api/info/", views.info_api, name="info_api"),
]