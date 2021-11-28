from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import MyForm
from .sugestionFramework.markov_generator import Markov_generator
#from .sugestionFramework.testFile import TestFile

# Create your views here.

TEMPOS = 24

sugestoesUsadas = []

def criarPossibilidadesDeOitavas(possibilidades):
    possibilidades_com_oitavas = []
    
    for oitava in reversed(range(0,9)):
        temp = []
        for possibilidade in possibilidades:
            temp.append(possibilidade+"-"+str(oitava))
        possibilidades_com_oitavas.append(temp)
    
    temp = possibilidades_com_oitavas[0][-1]
    possibilidades_com_oitavas[0] = [temp]
    possibilidades_com_oitavas[-1] = possibilidades_com_oitavas[-1][:3]


    return possibilidades_com_oitavas



markov_generator = Markov_generator()

markov_generator.createMarkovChainFor()
markov_generator.startToGenerate()

"""
teste = TestFile()

"""


def home(request, index_da_sugestao):

    form = MyForm(request.POST or None)

    if request.method == "POST":
       notesUsed = request.POST.getlist('notes')
       print(notesUsed)
    
    suggestions = markov_generator.getNextThereeSugestions()
    print(suggestions)

    sugestoes = suggestions 

    markov_generator.setSugestionToUse("0")

    possibilidades = ["B", "Bb","A","Ab","G","Gb","F","E","Eb","D","Db","C"]
    possibilidades_com_oitavas = criarPossibilidadesDeOitavas(possibilidades)

    tempos = [ 1,2,3 ]
    indices = ["0","1","2"]

    

    context = {
        "sugestoes": sugestoes,
        "indices" : indices,
        "sugestoesUsadas" : sugestoesUsadas,
        "possibilidades" : possibilidades,
        "possibilidades_com_oitavas" : possibilidades_com_oitavas,
        "tempos" : tempos
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
