from django.urls import path

from app4 import views

urlpatterns = [
    path('', views.home),
    path('add', views.add_fun),
    path('mul', views.mul_fun),
]
