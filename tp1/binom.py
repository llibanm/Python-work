
import functools
def factorielle_term_aux(a:int, a_1)-> int :
    if a_1 == 0:
        return a
    else :
        return factorielle_term_aux(a * a_1,a_1 -1)

def factorielle_term(a:int) -> int:
    if a == 0 :
        return a
    else :
        return factorielle_term_aux(a,a-1)
    


def binom(n : int, k :int) -> int:

    if k == 0 or k == n:
        return 1
    
    elif k < 0 or n < 0:
        print("k and/or n are lesser than 0")
        return -1

    else :
        return factorielle_term(n) // ( (factorielle_term(k)) * factorielle_term(n-k) )
    

#def binom_memo
#calculer les termes et les mettre sur le dic
#les clés seront les arguments

def binom_memo(n : int, k : int) ->int:

   

    dictionnaire : dict[tuple[int,int],int] = {}

    dictionnaire[(n,k)] = binom(n,k)

    

    return dictionnaire[(n,k)]

if __name__=="__main__":

    #print(binom_memo(100,50))

    pass    