# content of tp2/arraylist.py
from dataclasses import dataclass
from typing import List

@dataclass
class ArrayList:
    """User-defined type for List ADT implemented with static arrays."""
    # TODO: add your attributes here

    tab : list[int]
    max_size : int
    size : int 
    fin : int


def al_new(m: int = 10, l: list[int] | None = None) -> ArrayList:
    #raise NotImplementedError("ArrayList al_new function not implemented yet")
    if l is None:
        new_arr = ArrayList(
            tab=[],
            max_size=m,
            size=0,
            fin=-1
        )
    else:
        if len(l) <= m:
                    new_arr = ArrayList(
            tab = l.copy(),
            max_size=m,
            size=len(l),
            fin=len(l)-1
        )    
        else :
            raise AssertionError 
    return new_arr    
    



def al_len(tab: ArrayList) -> int:
    return tab.size


def al_is_empty(tab: ArrayList) -> bool:
    return tab.size<=0


def al_str(tab: ArrayList) -> str:
   # raise NotImplementedError("ArrayList al_str function not implemented yet")
    res :  str =""
    res+="["
    
    if al_is_empty(tab) :
        return '[]'
    
    tmp = tab.tab 

    for i in range(tab.size):
        #print(tmp[i])
        res+= str(tmp[i])
        #print(res)

        if i != tab.size -1:
            res+="," + " "
             
    
    res+="]"

    return res    
    

    
   


def al_get(tab: ArrayList, i: int) -> int:
   # raise NotImplementedError("ArrayList al_get function not implemented yet")

   if i > tab.size-1 or i < 0:
       raise IndexError(f"Index{i} out of bounds")
   return tab.tab[i]


   



def al_set(tab: ArrayList, i: int, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_set function not implemented yet")


def al_lookup(tab: ArrayList, item: int) -> int | None:
    raise NotImplementedError("ArrayList al_lookup function not implemented yet")


def al_remove(tab: ArrayList, i: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_remove function not implemented yet")


def al_insert(tab: ArrayList, i: int, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_insert function not implemented yet")


def al_prepend(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_prepend function not implemented yet")


def al_append(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_append function not implemented yet")


def al_extend(tab1: ArrayList, tab2: ArrayList) -> ArrayList:
    raise NotImplementedError("ArrayList al_extend function not implemented yet")

if __name__=="__main__":
    a : ArrayList = al_new(10,[1,2,3,4])
    print(a)
   #print(al_get(a))

    pass