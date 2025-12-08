
def hashcode_binary(s:str) -> int:

    return int.from_bytes(str.encode(s))


def hashcode_polynomial(s: str) -> int:

    res : int = 0

    for i in s:
        
        res += hashcode_binary(i) * 47

    return res    



"""def hashing_dico():
        
    dictionnary : dict[int,str] = {}

    with open('tp6/dicos/liste.de.mots.francais.frgut.txt','r') as f:
        line = f.readline()
        while line:
            dictionnary[hash(line)] = line
    
      """


def is_primal_number(m):
    
     
def compress_mod(n: int, m: int) -> int:
    raise NotImplemented        



if __name__=='__main__':

    #print(int.from_bytes( str.encode("lo")))
    #print(hashcode_polynomial("lol"))

    
    dict = hashing_dico()
    

    pass