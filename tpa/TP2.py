import math
from collatz import collatz_altitude,collatz_lifetime,collatz_series
from math import log2,log10


seed: int = 1999
index: int = collatz_lifetime(seed)
series: list[int] = collatz_series(seed,index)
height: int = collatz_altitude(seed)

#print(f"La suite de Collatz pour N={seed} "
#      f" a une durée de vie de {index}, une altitude de {height}\n"
#      f"et ses premiers termes sont {series[:10]}"
#      )

# Exercice 3

Point = tuple[float # x
              ,float] # y

def distance_et_barycentre(A:Point, B:Point) -> tuple[float,Point]:
    
    xA,yA = A
    xB,yB = B

    distance = math.sqrt( (xB-xA)*2 + (yB - yA)*2)
    
    xCentre = (xA + xB)/2
    yCentre = (yA +yB)/2

    Centre : Point = (xCentre,yCentre,)

    res : tuple = (distance,Centre,)

    return res

#Un : tuple[float,float] = (3.4,5.6)
#Deux : tuple[float,float] = (7,12)

#print( distance_et_barycentre(Un,Deux))

def dict_carre()->dict[int,int]:
    
    dict_res:dict[int,int]={}

    i = 0
    while i < 100:
        dict_res[i] = i**2
        i+=1
    return dict_res

#print(dict_carre())

def dict_list(l1 : list,l2 : list) -> dict: # we assume that both of these lists have equal length
    
    dict_res :dict={}


    for i in range(len(l1)):
        
        dict_res[ l1[i] ] = l2[i]
    
    return dict_res

l1 = ['orange','42',32]
l2 = ['color','number_string','number']

#print( dict_list(l1,l2))

def dict_average_value(a:dict[str,int]) -> int:
    res = 0
    count = 0

    for k,v in a.items():
        res+=v
        count+=1
    return (res//count)

dict_a :dict[str,int] = { 'answer':30 , 'lol':48, 'liban':32 }

#print(dict_average_value(dict_a))

# str,int

def list_tuples_from_dict( a:dict[str,int] ) : # trasform dict into tuples

    res : list[ tuple[str,int]] = []
    i = 0

    for k,v in a.items():
        res.append((k,v))
        i+=1

    return res

def reverse_sort( a :list[ tuple[str,int]] ) : # reverse sort the tuples
    return sorted(a
                  ,key= lambda x:x[1]
                  ,reverse=True)

"""def dict_from_reverse_sorted_tuples( a :list[ tuple[str,int]] ) : # remake a dict based on new sorted tuples

    sorted_dict : dict[str,int] = {}

    for i in range(len(a)):
        sorted_dict[ a[i][0] ] = a[i][1]
    return sorted_dict    """

def list_from_tuples( a:list ): # extract the sorted keys from dict
    sorted_list=[]

    for i in range(len(a)):
        sorted_list.append(a[i][0])
    return sorted_list    


def reverse_sorted_dict(a:dict[str,int] ):
    
  return list_from_tuples ( reverse_sort (  list_tuples_from_dict(  a )  ) )


# print( reverse_sorted_dict(dict_a) )


seq = "aucucggucgaccgcgcuuucaucgucggcaaagucaagaucccg"

#print(len(seq))

def acides_aminés(seq:str):
    
   res = set[str] 

def varargs(*args):
    return args[::-1]
              


print(varargs('liban',42,39,True))