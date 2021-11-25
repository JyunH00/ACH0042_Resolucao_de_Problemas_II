from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

TEMPOS = 24

sugestoesUsadas = []

def home(request, index_da_sugestao):

    
    #if index_da_sugestao.isupper():
    #    sugestoesUsadas.append(index_da_sugestao+"--> ")

    sugestoes = ["C#","G","D"] # getNext()

    
    possibilidades = ["B","A#","A","G#","G","F#","F","E","D","C#","C"]

    possibilidades_com_oitavas = []
    
    for oitava in reversed(range(0,9)):
        temp = []
        for possibilidade in possibilidades:
            temp.append(possibilidade+str(oitava))
        possibilidades_com_oitavas.append(temp)
    
    temp = possibilidades_com_oitavas[0][-1]
    possibilidades_com_oitavas[0] = [temp]
    possibilidades_com_oitavas[-1] = possibilidades_com_oitavas[-1][:3]

    print(possibilidades_com_oitavas)

    tempos = [ i for i in range(TEMPOS) ]


    indices = ["0","1","2"]

    index_da_sugestao = 1

    context = {
        "index": index_da_sugestao,
        "sugestoes": sugestoes,
        "indices" : indices,
        "sugestoesUsadas" : sugestoesUsadas,
        "possibilidades" : possibilidades,
        "possibilidades_com_oitavas" : possibilidades_com_oitavas,
        "tempos" : tempos,
    }
    return render(request, 'application/Pagina_principal.html', context)

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