from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>welcome to while loops</h1>")


def prime_fun(request):
    f = 0
    x = 10
    i = 2
    while i <= (x / 2):
        if (x % i) == 0:
            f = 1
            break
        i = i + 1
    if f == 0:
        prime = f"yes,{x} is a prime"
    else:
        prime = f"no is not a prime"
    return HttpResponse(f"<h1> {prime} </h1>")


def palindrome_fun(request):
    n = 121
    temp = n
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    if n == rev:
        palindrome = f"The {n} number is palindrome"
    else:
        palindrome = f"not a palindrome"
    return HttpResponse(f"<h1> {palindrome}</h1>")


def armstrong_fun(request):
    n = 407
    s = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        s += rem ** 3
        temp //= 10
    if n == s:
        armstrong = f"yes,{n} is armstrong"
    else:
        armstrong = f"no is not a armstrong"
    return HttpResponse(f"<h1> {armstrong}</h1>")
