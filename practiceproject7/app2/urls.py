from django.urls import path

from app2 import views

urlpatterns = [
    path("home",views.app_fun),
    path("add",views.add_fun),
    path("pop",views.pop_fun),
]