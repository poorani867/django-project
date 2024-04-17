from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def app_fun(request):
    return HttpResponse("<h1> welcome to project7 app2</h1>")


def add_fun(request):
    s={11,12,13,14}
    app2=s.add(15)
    return HttpResponse(f"<h1> The added number is {s}</h1>")


def pop_fun(request):
    s = {11, 12, 13, 14}
    app2 = s.pop()
    return HttpResponse(f"<h1> The pop number is {s}</h1>")