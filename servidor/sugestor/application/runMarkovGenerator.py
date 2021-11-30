from sugestionFramework.markov_generator import Markov_generator


m = Markov_generator()

m = Markov_generator()
m.createMarkovChainFor()
m.startToGenerate()

suggestions = m.getNextThereeSugestions()
print(suggestions)

#sugestion_to_use = int(input("select the suggestion "))
m.setSugestionToUse("0")

suggestions = m.getNextThereeSugestions()
print(suggestions)
#sugestion_to_use = int(input("select the suggestion "))
m.setSugestionToUse("-1")

suggestions = m.getNextThereeSugestions()
print(suggestions)
#sugestion_to_use = int(input("select the suggestion "))
m.setSugestionToUse("2")

suggestions = m.getNextThereeSugestions()
print(suggestions)
#sugestion_to_use = int(input("select the suggestion "))
m.setSugestionToUse("2")
m.saveMidiAs()