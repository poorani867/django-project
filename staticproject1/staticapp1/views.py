from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def add_fun(request):
    return render(request,'add.html')


def display_fun(request):
    return render(request,'display.html')


def update_fun(request):
    return render(request,'update.html')