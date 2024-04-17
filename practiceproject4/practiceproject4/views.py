from django.http import HttpResponse


def home(request):
    return HttpResponse("welcome to for loop")


def even_fun(request):
    e = [10, 11, 12, 13, 15, 17, 14, 16, 18, 20, 19]
    l = []
    for i in e:
        if i % 2 == 0:
            l = l + [i]

    return HttpResponse(f"<h1>{l}</h1>")


def odd_fun(request):
    e = [10, 11, 12, 13, 15, 17, 14, 16, 18, 20, 19]
    l = []
    for i in e:
        if i % 2 == 1:
            l = l + [i]

    return HttpResponse(f"<h1>{l}</h1>")


def even_index_fun(request):
    e = [10, 11, 12, 13, 15, 17, 14, 16, 18, 20, 19]
    even_index_pos = []
    for i in range(len(e)):
        if i % 2 == 0:
            even_index_pos = even_index_pos + [e[i]]

    return HttpResponse(f"<h1>{even_index_pos}<h1>")


def odd_index_fun(request):
    e = [10, 11, 12, 13, 15, 17, 14, 16, 18, 20, 19]
    odd_index_pos = []
    for i in range(len(e)):
        if i % 2 == 1:
            odd_index_pos = odd_index_pos + [e[i]]

    return HttpResponse(f"<h1>{odd_index_pos}<h1>")
