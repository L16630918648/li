"""
URL configuration for my_site project.

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
from django.urls import path, re_path
from li_demo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello',views.hello),
    path('inf_out/<str:name>/<int:age>',views.inf_out),
    re_path(r'^(?P<x>\d+)/112/(?P<y>\d+)/?$',views.postion),
    path('time',views.time),
    path('api',views.api_info),
    path('file_page',views.file_page),
    path("download/<str:file_name>", views.file, name="file"),
    path("back_first",views.back_first,name = "first"),
    path("page_2006",views.page_2006),
    path("room/<str:name>",views.room,name="room"),
    path("index_redirect",views.index_redirect),
    path("page_GET",views.page_GET),

]
