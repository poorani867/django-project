from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1> welcome to multiple apps</h1>")


def home_fun(request):
    return HttpResponse("<h1> welcome to app1 function </h1>")


def app_fun(request):
    return HttpResponse("<h1> welcome to app2 function </h1>")