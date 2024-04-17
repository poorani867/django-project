from django.urls import path

from fourthapp import views

urlpatterns = [
    path('',views.home),
    path('display',views.display_fun),
]