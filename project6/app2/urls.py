from django.urls import path

from app2 import views

urlpatterns = [
    path("home",views.app_fun),
    path("sum1",views.sum_fun),
]
