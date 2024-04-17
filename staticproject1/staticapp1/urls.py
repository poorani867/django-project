from django.urls import path

from staticapp1 import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_fun, name='add'),
    path('display/', views.display_fun, name='display'),
    path('update/', views.update_fun, name='update'),

]
