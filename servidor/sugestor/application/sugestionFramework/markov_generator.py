# Este arquivo teste, serve para criarmos diferentes tipos de cadeias de Markov, de acordo com um gênero musical específica

from .markov_chain import MarkovChain
from .generator import Generator
from .parser2 import Parser2

class Markov_generator:

    def __init__(self):
        self.final_markov = MarkovChain()
        self.name_of_out = ""
        self.counter = 0
        self.initCoversionMaps()
        self.lastSuggestionsUsed = []
        self.lastNoteUsed = ""

    def initCoversionMaps(self):
        self.numberToOctavesMap = {}
        self.numberToNotesMap = {}
        noteNumbers = [i for i in range(12,108)]

        #notesInLetters = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        notesInLetters = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
    

        octaveCounterNotes = 0
        octaveCounterTones = 1

        # Tone to number map
        for noteNumber in noteNumbers:
            if octaveCounterNotes == 12:
                octaveCounterNotes = 0
                octaveCounterTones += 1
            self.numberToOctavesMap[noteNumber] = str(octaveCounterTones)
            octaveCounterNotes += 1

        notesCounter = 0
        # Note to number map
        for noteNumber in noteNumbers:
    
            if notesCounter == 12:
                notesCounter = 0

            note = notesInLetters[notesCounter]

            self.numberToNotesMap[noteNumber] = note
            notesCounter += 1

    def create_markov(self,paste, n_music, name_of_out = 'out'):

        testePath = '/home/sonia/Documentos/ACH0042_Resolucao_de_Problemas_II/servidor/sugestor/application/sugestionFramework/genre_yiruma/1.mid'
        toAdd = 'application/sugestionFramework/'
        for name in range(1, n_music + 1):
            chain = Parser2(f'{toAdd}/{paste}/{name}.mid').get_chain()
            #chain = Parser2(testePath).get_chain()
            self.final_markov.merge(chain)
            
        #Generator.load(final_markov).generate_paused_test(f'saidas_markov/{name_of_out}.mid')
        
        sourceFile = open(f'application/sugestionFramework/saidas_markov/{name_of_out}.txt', 'w')
        print_markov = self.final_markov.print_as_matrix()
        print(print_markov, file=sourceFile)
        sourceFile.close()
        
        return self.final_markov

    def teste_de_chamada(self):
        
        # Gênero disco
        """
        final_disc = create_markov('genre_disco', 5, 'out_disco' )
        

        # Gênero reggae
        
        final_reggae = create_markov('genre_reggae', 6, 'out_reggae' )
        
        # Gênero rock
        final_classic = create_markov('genre_rock', 1, 'out_rock')
        """
        """
        # Gênero classico
        final_classic = create_markov('genre_classic', 5, 'out_classic')
        """
        # Teste com apenas 1 música

        print("calling test folder")
        
    def createMarkovChainFor(self):
        final_yiruma = self.create_markov('genre_yiruma', 1, 'out_yiruma')
        self.name_of_out = 'genre_yiruma'
    
    def startToGenerate(self):
        self.generator = Generator(self.final_markov)
        self.generator.startToGenerate()
    
    def setSugestionToUse(self, index):
        self.generator.setSugestionToUse(index)

    def getLastPastSugestions(self):
        return self.lastSuggestionsUsed
    
    def getNextThereeSugestions(self):
        self.lastSuggestionsUsed = self.getOnlyNotes(self.generator.getNextSugestions())
    
    def saveMidiAs(self):
        self.generator.saveMidi(f'application/sugestionFramework/saidas_markov/{self.name_of_out}.mid')
    
    def getOnlyNotes(self, suggestions):
        only_notes = []
        letter_notes = []

        for suggestion in suggestions:
            only_notes.append(str(suggestion.note))
        
        for index in range(len(only_notes)):
            letter_notes.append(self.fromNumberToLetter(int(only_notes[index])))

        return letter_notes

    def fromNumberToLetter(self, noteInNumber):
        
        octaveOfNote = str(self.numberToOctavesMap[noteInNumber])
        letterOfNote = str(self.numberToNotesMap[noteInNumber])

        return letterOfNote+"-"+octaveOfNote

    def fromLetterToNumber(self, noteInLetter):
        
        splited = noteInLetter.split("-")

        noteNumbers = [ i for i in range(12,108) ]

        notesInLetters = { "C":0,"C#":1,"D":2,"D#":3,"E":4,"F":5,"F#":6,"G":7,"G#":8,"A":9,"A#":10,"B":11 }

        noteNumbersMatrix = []
        indexNumbers = 0

        # Generate matrix
        for note in range(8):
            octave = []
            for i in range(12):
                octave.append(noteNumbers[indexNumbers])
                indexNumbers += 1
            noteNumbersMatrix.append(octave)
                
        numberOfNote = noteNumbersMatrix[int(splited[1])-1][notesInLetters[splited[0]]]

        return numberOfNote

    """ 
if __name__ == '__main__':

    teste = Markov_generator()
    teste.createMarkovChainFor()
    teste.startToGenerate()
    
        

    print(teste.fromNumberToLetter(56))
    print(teste.fromNumberToLetter(40))
    print(teste.fromNumberToLetter(104))
    print(teste.fromNumberToLetter(31))
    print(teste.fromNumberToLetter(49))
    
    
    print(teste.fromLetterToNumber("C-8")) # 96
    print(teste.fromLetterToNumber("B-5")) # 71
    print(teste.fromLetterToNumber("C-5")) # 60
    print(teste.fromLetterToNumber("G#-2")) # 32
    print(teste.fromLetterToNumber("D-4")) # 50
    
  
    
    
    suggestions = teste.getNextThereeSugestions()
    print(suggestions)

    #sugestion_to_use = int(input("select the suggestion "))
    teste.setSugestionToUse("0")

    suggestions = teste.getNextThereeSugestions()
    print(suggestions)
    #sugestion_to_use = int(input("select the suggestion "))
    teste.setSugestionToUse("-1")

    suggestions = teste.getNextThereeSugestions()
    print(suggestions)
    #sugestion_to_use = int(input("select the suggestion "))
    teste.setSugestionToUse("2")

    suggestions = teste.getNextThereeSugestions()
    print(suggestions)
    #sugestion_to_use = int(input("select the suggestion "))
    teste.setSugestionToUse("2")
    teste.saveMidiAs()
  
    """
    