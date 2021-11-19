from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

sugestoesUsadas = []

def home(request, index_da_sugestao):
    if index_da_sugestao.isupper():
        sugestoesUsadas.append(index_da_sugestao+"--> ")

    sugestoes = ["C#","G","D"]

    
    possibilidades = ["C","C#","D","E","F","F#","G","G#","A","A#","B"]


    indices = ["0","1","2"]

    context = {
        "index": index_da_sugestao,
        "sugestoes": sugestoes,
        "indices" : indices,
        "sugestoesUsadas" : sugestoesUsadas,
        "possibilidades" : possibilidades
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