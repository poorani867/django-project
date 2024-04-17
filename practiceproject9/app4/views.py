from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')


def add_fun(request):
    number1 = int(request.POST['txtnumber1'])
    number2 = int(request.POST['txtnumber2'])
    add = number1 + number2
    data = {"number1": number1, "number2": number2,'add':add}

    return render(request, 'add.html', data)


def mul_fun(request):
    number1 = int(request.POST['txtnumber1'])
    number2 = int(request.POST['txtnumber2'])
    mul = number1 * number2
    data = {"number1": number1, "number2": number2,'mul':mul}

    return render(request, 'mul.html', data)
