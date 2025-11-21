# content of tp3/linkedlist.py
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from typing import Any



@dataclass
class LinkedList:
    # TODO: add attributes here
    #head : Cell 
    #tail : Cell
    sentinelle : Cell ## son suiv va être le dbut de la liste et sont pred va être sa fin
    size : int

   

@dataclass(eq=False)
class Cell:
    item : int
    # TODO: add attributes here
    pred : Cell | None
    suiv : Cell | None
    



def ll_new(initial_l: list[int] | None = None) -> LinkedList:
    #raise NotImplementedError("LinkedList ll_new function not yet implemented")
    
    #s : Cell = Cell(0,None,None) #sentinelle servant 

    new : LinkedList = LinkedList(

        sentinelle= Cell(
            item=0,
            pred=None,
            suiv=None,
        ),


        size=0,

    )

    new.sentinelle.pred=new.sentinelle
    new.sentinelle.suiv=new.sentinelle

    if initial_l !=None:

        for i in range(len(initial_l)):
            
            ll_append(new,initial_l[i])
            
            
    
    return new


def ll_is_empty(l: LinkedList) -> bool:
    #raise NotImplementedError("LinkedList ll_is_empty function not yet implemented")
    return l.sentinelle.suiv==l.sentinelle and l.sentinelle.pred==l.sentinelle and l.size==0



def ll_head(l: LinkedList) -> Cell:
    #raise NotImplementedError("LinkedList ll_head function not yet implemented")
   
    if l.sentinelle.suiv == None:
        raise IndexError
    
    else :
        return l.sentinelle.suiv


def ll_tail(l: LinkedList) -> Cell:
    if l.sentinelle.pred == None:
        raise IndexError
    
    else :
        return l.sentinelle.pred


def ll_append(l: LinkedList, item: int) -> Cell:
    #raise NotImplementedError("LinkedList ll_append function not yet implemented")

    new_cell : Cell

    if ll_is_empty(l):
        new_cell = Cell (
            item=item,
            suiv=l.sentinelle,
            pred=l.sentinelle
        )

        l.sentinelle.suiv=new_cell
        l.sentinelle.pred=new_cell
        l.size+=1
#        print(l.sentinelle.pred)
#        print(l.sentinelle.suiv)

    else :

        tmp : Cell = ll_tail(l) # prends la derniere cell de la liste

        new_cell = Cell( # new_cell prends comme pred la fin de la liste et son suiv est la sentinelle
            item=item,
            pred=tmp,
            suiv=l.sentinelle
        )

        l.sentinelle.pred = new_cell # la sentinelle prends comme val pred la nouvelle cell

        tmp.suiv = new_cell # la fin de la list n'est plus la fin de la liste et prends new_cell comme la nouvelle fin
        l.size+=1

    return new_cell
"""
    coût pour le dbut : O(1)
    coût pour la fin : O(1)
    
"""

def ll_next(c:Cell) -> Cell:
    if c.suiv != None:
        return c.suiv
    else : raise IndexError

def ll_prev(c:Cell) -> Cell:
    if c.pred != None:
        return c.pred
    else : raise IndexError

def ll_iter(l: LinkedList, reverse: bool=False) -> Iterator[Cell]:
    '''
        if not ll_is_empty(l):                  # vérifie que la liste n'est pas vide
        current: Cell = ll_head(l)              # initialise la variable current à la tête de liste
        if reverse:                             # parcourt la liste en sens inverse
            while current.prev is not None:     # tant qu'il y a des maillons
                yield current                   # "return" le maillon courant et gèle l'exécution
        else:                                   # idem, dans le sens de la liste
            while current.next is not None:
                yield current
    '''
    #raise NotImplementedError("LinkedList ll_iter_cells function not yet implemented")

    current : Cell = Cell(
        item=0,
        pred=None,
        suiv=None
    )

    if not ll_is_empty(l):
        
        if reverse:
            
            current = ll_tail(l)

            while current != l.sentinelle:
                yield current
                current = ll_prev(current)


        else :

            current = ll_head(l)

            while current != l.sentinelle:
                yield current
                current = ll_next(current)        





def ll_len(l: LinkedList) -> int:
    return l.size


def ll_str(l: LinkedList) -> str:
    #raise NotImplementedError("LinkedList ll_str function not yet implemented")

    res : str =""
    res+="["

    if ll_is_empty(l):
        return '[]'

    size = l.size
    tmp = ll_head(l)

    for i in range(size):
        res += str(tmp.item)
        
        if i != size-1:
            res+="," + " "
            tmp = ll_next(tmp)

    res+="]"

    return res    

 


def ll_lookup(l: LinkedList, item: int) -> Cell | None:
    #raise NotImplementedError("LinkedList ll_lookup function not yet implemented")

    if ll_is_empty(l):
        return None
    
    for i in ll_iter(l):
        if i.item==item:
            return i

    return None    


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    #raise NotImplementedError("LinkedList ll_cell_at function not yet implemented")

    if i < 0 or i > ll_len(l):
        raise IndexError("index out of range")
    
    tmp = ll_head(l)

    for c in range(ll_len(l)):
        if c == i:
            return tmp
        tmp = ll_next(tmp)
        
    raise IndexError("index out of range")  
        
        


def ll_prepend(l: LinkedList, item: int) -> Cell:
    #raise NotImplementedError("LinkedList ll_prepend function not yet implemented")

    new_head : Cell

    if ll_is_empty(l):
       new_head = Cell (
           item=item,
           pred=l.sentinelle,
           suiv=l.sentinelle)
       
       l.sentinelle.suiv=new_head
       l.sentinelle.pred=new_head

       l.size+=1

       return new_head



    new_head  = Cell(
        item= item,
        pred=l.sentinelle,
        suiv=ll_head(l))

    former_head = ll_head(l)
    former_head.pred = new_head

    l.sentinelle.suiv = new_head     

    l.size+=1

    return new_head
    


def ll_insert(l: LinkedList, item: int, next_to: Cell) -> Cell:
    #raise NotImplementedError("LinkedList ll_insert function not yet implemented")

    new_cell : Cell

    if ll_is_empty(l):
        ll_append(l,item)
    
    next_to_suiv : Cell

    for i in ll_iter(l):
        if i == next_to:
            next_to_suiv = ll_next(next_to)
            
            new_cell = Cell(
                item=item,
                pred=next_to,
                suiv=next_to_suiv
            )

            next_to.suiv = new_cell
            next_to_suiv.pred = new_cell
            l.size+=1

            return new_cell


    raise IndexError('Cell not found')

            
                   


def ll_remove(l: LinkedList, cell: Cell) -> int:
    #raise NotImplementedError("LinkedList ll_remove function not yet implemented")

    if ll_is_empty(l):
        raise IndexError("empty linkedlist")
    
    found = False

    for i in ll_iter(l):
        if i == cell:
            found=True
            break

    if not found:
        raise IndexError("Value not found") 

    prev_cell = ll_prev(cell)
    next_cell = ll_next(cell)


    prev_cell.suiv = next_cell
    next_cell.pred = prev_cell

    cell.suiv = None
    cell.pred = None
    

    l.size-=1

    return cell.item
    
        
    


def ll_extend(l1: LinkedList, l2: LinkedList) -> None:
    raise NotImplementedError("LinkedList ll_extend function not yet implemented")

if __name__=='__main__':

    a : LinkedList = ll_new([1,2,3,4,5,6,7,8])
    b : LinkedList = ll_new([])

    print(ll_str(a) + " |",a.size)

    #ll_prepend(a,0)
    #ll_prepend(a,-1)

    next_to_variable :Cell = ll_next(ll_next(ll_head(a))) #3

    ll_insert(a,-1,next_to_variable)

    print(ll_str(a) + " |",a.size)

    to_del = ll_next(next_to_variable)

    print(ll_remove(a,to_del)) # deleting -1

    print(ll_str(a) + " |",a.size)

    #print(ll_remove(a,to_del))
    print(ll_remove(b,to_del))




    pass