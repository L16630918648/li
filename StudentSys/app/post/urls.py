from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('post/create/', views.post_create_page, name='create'),
    path('post/api/create/', views.post_create_api, name='push'),
    path('post/mine/', views.post_mine, name='mine'),
]