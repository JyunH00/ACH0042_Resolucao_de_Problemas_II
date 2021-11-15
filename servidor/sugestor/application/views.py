from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request, index_da_sugestao):

    sugestoes = ["A","B","C"]

    context = {
        "index": index_da_sugestao,
        "sugestoes": sugestoes
    }
    return render(request, 'application/input.html', context)

def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})