import random

def is_list_sorted(l:list)-> bool:
    for i in range(1,len(l)):
        if not l[i-1] < l[i]:
            return False
        
    return True     

def stupidsort(seq: list[int]) -> list[int] :

    if seq == []:
        return []
    
    elif is_list_sorted(seq):
        return seq

    else :

        for i in range(len(seq)-1,1,-1):
            
            if is_list_sorted(seq):
                break

            seed = random # selection

            j = seed.randint(0,i)

            tmp = seq[i] # permutation
            seq[i] = seq[j]
            seq[j] = tmp

            #print(seq)

    return seq


if __name__=='__main__':

    a : list = [9,7,1,3,9,0,1,4]
    a = stupidsort(a)
    print(a)
    pass

        
