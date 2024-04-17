from django.urls import path

from secondapp import views

urlpatterns = [
    path('apphome',views.app_home),
    path('even_list',views.even_fun),
    path('even_list_sum',views.even_sum_fun),
]