from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1> welcome to project 7</h1>")


def home_fun(request):
    return HttpResponse("<h1> welcome to project app1</h1>")


def append_fun(request):
    x = [1, 2, 3, 4]
    app1 = x.append(6)
    return HttpResponse(f"<h1> append number is {x} </h1>")


def extend_fun(request):
    x = [1, 2, 3, 4]
    y = [5, 6, 7]
    app1 = x.extend(y)
    return HttpResponse(f'<h1> extend number is {x}</h1>')


def pop_fun(request):
    x = [10, 20, 30, 40]
    app1 = x.pop(2)
    return HttpResponse(f"<h1> pop number is{x}</h1>")


def remove_fun(request):
    x = [10, 20, 30, 40]
    app1 = x.remove(10)
    return HttpResponse(f"<h1>  remove number is{x}</h1>")