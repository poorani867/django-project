from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def display(request):
    global res
    name = request.POST['txtname']
    n1 = int(request.POST['txtpython'])
    n2 = int(request.POST['txtjava'])
    n3 = int(request.POST['txtmysql'])
    n4 = int(request.POST['txthtml'])
    n5 = int(request.POST['txtdjango'])
    v1 = request.POST['operations']
    if v1 == 'TOTAL':
        res = (n1 + n2 + n3 + n4 + n5)
    elif v1 == 'PERCENTAGE':
        res = ((n1 + n2 + n3 + n4 + n5) / 250) * 100
    elif v1 == 'GRADE':
        p = ((n1 + n2 + n3 + n4 + n5) / 250) * 100
        if p > 90:
            res = "A(Excellent)"
        elif p > 80 and p < 90:
            res = 'B(Very good)'
        elif p > 70 and p < 80:
            res = 'C(Good)'
        elif p > 60 and p < 70:
            res = 'D(Average)'
        elif p > 50 and p < 60:
            res = 'E(Poor)'
        else:
            res = 'F(Fail)'
    elif v1 == 'STATUS':
        r = ((n1 + n2 + n3 + n4 + n5) / 250) * 100
        if r > 50:
            res = 'PASS(Excellent)'
        else:
            res = 'FAIL'
    data = {'name': name, 'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 'res': res}
    return render(request, "home.html", data)
