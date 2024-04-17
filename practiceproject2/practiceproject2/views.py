from django.http import HttpResponse


def home(request):
    return HttpResponse("welcome to conditions")


def big_fun(request):
    a = 10
    b = 20
    c = 30
    if a > b and a > c:
        big = a
    elif b > c:
        big = b
    else:
        big = c
    return HttpResponse(f"<h1>biggest of three numbers is{big}</h1>")


def fib_fun(request):
    i = 0
    j = 1
    n = 0
    l = []
    while n < 10:
        l = l + [i]
        i, j = j, i + j
        n = n + 1
    return HttpResponse(f"<h1>first 10 fibonacci values are {l}</h1>")


def small_fun(request):
    a = 10
    b = 30
    c = 100
    if a < b and a < c:
        small = a
    elif b < c:
        small = b
    else:
        small = c
    return HttpResponse(f"<h1>smallest among all numbers is{small}</h1>")


def even_fun(request):
    x=10
    if x%2==0 and x>0:
        even = f"yes,{x} is even number"
    else:
        even = f"no,{x}is not even number"
    return HttpResponse(f"<h1> {even}</h1 ")


def odd_fun(request):
    x=55
    if x%2!=0 and x>0:
        odd = f"yes,{x} is odd number"
    else:
        odd = f"no,{x} is not odd number"
    return HttpResponse(f"<h1> {odd}</h1>")