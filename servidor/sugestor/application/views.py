from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import MyForm
from .sugestionFramework.markov_generator import Markov_generator
import json
#from .sugestionFramework.testFile import TestFile

# Create your views here.

TEMPOS = 24

sugestoesUsadas = []

def criarPossibilidadesDeOitavas(possibilidades):
    possibilidades_com_oitavas = []
    
    for oitava in reversed(range(0,9)):
        temp = []
        for possibilidade in possibilidades:
            temp.append(possibilidade+str(oitava))
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

notesUsed = []

sugestoes = []


def home(request, index_da_sugestao):



    # GERAR SUGESTÕES INICIAIS DA MUSICA
    if markov_generator.counter == 0:
        markov_generator.getNextThereeSugestions()
        markov_generator.counter +=1

    # GRAVAR NOTAS JÁ USADAS
    form = MyForm(request.POST or None)
    if request.method == "POST":
       for note in request.POST.getlist('notes'):
           if markov_generator.counter != 0 :
               splited = note.split("-")
               notesUsed.append("".join(splited[0:2]))
               markov_generator.getNextThereeSugestions()
               
               sugestoesGeradas = markov_generator.getLastPastSugestions()
               print(sugestoesGeradas)
       print(notesUsed)
       markov_generator.counter +=1

       
    
    # SETAR SUGESTÃO UTILIZADA
    if index_da_sugestao != "favicon.ico" and index_da_sugestao != markov_generator.lastNoteUsed and markov_generator.counter != 0:

        print("SETANDO SUGESTÃO USADA")
         

        sugestoesGeradas = markov_generator.getLastPastSugestions()
        print("ESSA FOI AS ULTIMAS SUGERIDAS : "+str(markov_generator.getLastPastSugestions()))
        print("ESSA FOI A ULTIMA NOTA SELECIONADA "+index_da_sugestao)
        count = 0

        splited = index_da_sugestao.split("-")
        converted = "".join(splited)


        notesUsed.append(converted)
        indexAUsar = -1
        for sugestoesGerada in sugestoesGeradas:
            
            if sugestoesGerada == index_da_sugestao:
                indexAUsar = count
            count += 1

        markov_generator.lastNoteUsed = index_da_sugestao
        
        print("EU VOU USAR ESSE INDEX "+str(indexAUsar))
        print("ULTIMA NOTA USADA "+markov_generator.lastNoteUsed)
        
        if indexAUsar != -1:
            markov_generator.setSugestionToUse(str(indexAUsar))
        else:
            markov_generator.setSugestionToUse("-1")

        

        # GERAR PROXIMAS SUGESTÕES
        markov_generator.getNextThereeSugestions()
    

    possibilidades = ["B", "Bb","A","Ab","G","Gb","F","E","Eb","D","Db","C"]
    possibilidades_com_oitavas = criarPossibilidadesDeOitavas(possibilidades)

    tempos = [ i for i in range(28) ]
    indices = ["0","1","2"]
    notas_usadas = json.dumps(notesUsed)
    print("NOTAS USADAS ")
    print(notesUsed)

    context = {
        "sugestoes": markov_generator.getLastPastSugestions(),
        "indices" : indices,
        "sugestoesUsadas" : sugestoesUsadas,
        "possibilidades" : possibilidades,
        "possibilidades_com_oitavas" : possibilidades_com_oitavas,
        "tempos" : tempos,
        "notesUsed" : notas_usadas
    }
    
    
    return render(request, 'application/Pagina_principal.html', context)
 
 
def login(request): 
     
  return render(request, 'application/Login.html')
 
def nav(request): 
     
  return render(request, 'application/Navegacao.html')
 
def perfil(request):
     
  return render(request, 'application/CriacaoPerfil.html')