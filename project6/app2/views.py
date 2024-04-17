from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def app_fun(request):
    return HttpResponse("<h1> welcome to app2 function </h1>")


def sum_fun(request):
    x = int(input("enter a number1:"))
    y = int(input("enter a number1:"))
    z = x + y
    return HttpResponse(f"sum of {x} and {y} is {z}")
