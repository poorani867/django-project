from django.urls import path

from sscorevalidation import views

urlpatterns = [
    path('',views.home),
    path('display',views.display)
]