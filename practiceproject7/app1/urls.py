from django.urls import path

from app1 import views

urlpatterns = [
    path("home",views.home_fun),
    path("append",views.append_fun),
    path("extend",views.extend_fun),
    path("pop",views.pop_fun),
    path("remove",views.remove_fun),

]