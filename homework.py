# Exercice premier doublon 

exo_1_list : list[str] = ["abcd","1234","abcd","liban","yonis"]

def exo1():
    for i in range(len(exo_1_list)):
        for j in range(len(exo_1_list)):

            if exo_1_list[i] == exo_1_list[j]:
                print(exo_1_list[i])
                return
            
exo1()            