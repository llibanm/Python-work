import random

def stupidsort(seq: list[int]) -> list[int] :

    for i in range(len(seq)-1,1,-1):

        seed = random # selection

        j = seed.randint(0,i)

        tmp = seq[i] # permutation
        seq[i] = seq[j]
        seq[j] = tmp

        #print(seq)

    return seq


if __name__=='__main__':

    a : list = [1,2,3,4,5,6,7,8,9,10]
    print("# before")
    print(a)
    print("# after")
    stupidsort(a)

    pass

        
