# Este arquivo teste, serve para criarmos diferentes tipos de cadeias de Markov, de acordo com um gênero musical específica

from markov_chain import MarkovChain
from generator import Generator
from parser2 import Parser2

def create_markov(paste, n_music, name_of_out = 'out'):
    
    final_markov = MarkovChain()
    
    for name in range(1, n_music + 1):
        chain = Parser2(f'{paste}/{name}.mid').get_chain()
        final_markov.merge(chain)
        
    Generator.load(final_markov).generate_paused(f'saidas_markov/{name_of_out}.mid')
    
    sourceFile = open(f'saidas_markov/{name_of_out}.txt', 'w')
    print_markov = final_markov.print_as_matrix()
    print(print_markov, file=sourceFile)
    sourceFile.close()
    
    return final_markov

if __name__ == "__main__":
    
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
    
    final_yiruma = create_markov('genre_yiruma', 1, 'out_yiruma')
    
