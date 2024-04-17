"""
URL configuration for practiceproject4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from practiceproject4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('even_list', views.even_fun),
    path('odd_list', views.odd_fun),
    path('even_index_list', views.even_index_fun),
    path('odd_index_list', views.odd_index_fun),
]
