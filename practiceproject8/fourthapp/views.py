from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def display_fun(request):
    name = request.GET['txtstudentname']
    std = request.GET['txtstudentclass']
    age = request.GET['txtstudentage']
    place = request.GET['txtstudetplace']
    blood_group = request.GET['rdblood group']
    return HttpResponse(f"<h1>student name is {name}<br>"
                        f"student  age is {age}<br>"
                        f"student class is {std}<br>"
                        f"student place is {place}<br>"
                        f"student blood group is {blood_group}</h1>")
