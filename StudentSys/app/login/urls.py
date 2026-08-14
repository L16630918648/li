from django.urls import path
from . import views

urlpatterns = [
    path("registered/", views.registered_index, name="registered"),
    path("api/registered/add/", views.registered_add, name="registerApi"),
    path("login/", views.login, name="login"),
    path('quit/',views.login_out, name='quit'),
    path("api/login/", views.login_api, name="login_api"),
]