from  tp2.util import StaticArray, alloc, nops

#— list_to_array(l) : crée un tableau StaticArray à partir d’une liste Python ℓ ;
#— random_array(m, a, b) : crée un tableau de taille 𝑚 rempli de nombres entiers aléatoires
#  tirés dans l’intervalle J𝑎, 𝑏K ;
#— nops(t) : retourne le nombre d’opérations de lecture et d’écriture réalisées dans le tableau 𝑡 ;
#— reset_nops(t) : met à zéro les compteurs d’opérations du tableau 𝑡.

def mode(tab : StaticArray) -> int :    
    #dict_ops = nops(tab)
    #res : int = dict_ops['nread'] + dict_ops['nwrite']
    
    past_occ : int = 0
    past_number : int = tab[0]

    for i in range(len(tab)):
        
        current_occ : int = 0
        current_number : int = tab[i]        
        
        for j in range(len(tab)):

            if tab[i] == tab[j]:
                
                current_occ+=1
                
                if current_occ > past_occ:
                    past_number = current_number
                    past_occ = current_occ
    

    #print(past_number,past_occ)
    print(nops(tab))
    return past_number
 

def cumulative_sum(tab : StaticArray) -> StaticArray:
    
    length = len(tab)
    
    if length <= 1:
        return tab
    
    tab_res : StaticArray = alloc(length)

    tmp = 0

    for i in range(len(tab)):
        tab_res[i] = tmp + tab[i]
        tmp = tab_res[i]
    
    return tab_res

""" Bonus
def duplicate_elimination(tab: StaticArray) -> StaticArray :

    length =  len(tab)

    if length <= 1:
        return tab
    
    tab_before = tab

    tab_after : StaticArray = alloc(length)

    for i in range(length):

        for j in range(length):
"""



if __name__ == "__main__":
    #mode()
    tab : StaticArray = alloc(5)
    tab[1] = 2
    tab[4] = 9
    print(cumulative_sum(tab))
    print(tab)
    print(nops(tab))
    

    pass 