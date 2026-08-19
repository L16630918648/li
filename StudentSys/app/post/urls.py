from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('post/create/', views.post_create_page, name='create'),
    path('post/api/create/', views.post_create_api, name='push'),
    path('post/mine/', views.post_mine, name='mine'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)