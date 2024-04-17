from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1>welcome to practice project</h1>")


def app_home(request):
    return HttpResponse("<h1>welcome to practice project app</h1>")


def even_fun(request):
    l = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
    l1 = []
    for i in l:
        if i % 2 == 0:
            l1 = l1 + [i]
    return HttpResponse(f"<h1> {l1}</h1>")


def even_sum_fun(request):
    l = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
    l1 = []
    s = 0
    for i in l:
        if i % 2 == 0:
            s = s + i
    return HttpResponse(f"<h1> The even sum{s}</h1>")
