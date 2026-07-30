"""
URL configuration for StudentSys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from login import views as login_views
from info import views as info_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("registered/", login_views.registered_index, name="registered"),
    path('api/registered/add/', login_views.registered_add, name='registerApi'),
    path('login/', login_views.login, name='login'),
    path('api/login/', login_views.login_api, name='login_api'),
    path("", info_views.index, name="index"),
    path("api/info/", info_views.info_api, name="info_api"),
]

# 需要在数组外边
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)