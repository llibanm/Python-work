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

    if initial_l !=None:

        for i in range(len(initial_l)):
            
            ll_append(new,initial_l[i])
            
            
    
    return new


def ll_is_empty(l: LinkedList) -> bool:
    #raise NotImplementedError("LinkedList ll_is_empty function not yet implemented")
    return l.sentinelle.suiv==None and l.sentinelle.pred==None and l.size==0



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

            current = ll_tail(l)

            while current != l.sentinelle:
                yield current
                current = ll_next(current)        





def ll_len(l: LinkedList) -> int:
    return l.size


def ll_str(l: LinkedList) -> str:
    #raise NotImplementedError("LinkedList ll_str function not yet implemented")

    if ll_is_empty(l):
        raise IndexError
    
    tmp_cell : Cell = ll_head(l)

    for i in range(l.size):
        print(tmp_cell.item)
    raise NotImplementedError("LinkedList ll_str function not yet implemented")



def ll_lookup(l: LinkedList, item: int) -> Cell:
    raise NotImplementedError("LinkedList ll_lookup function not yet implemented")


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    raise NotImplementedError("LinkedList ll_cell_at function not yet implemented")


def ll_prepend(l: LinkedList, item: int) -> Cell:
    raise NotImplementedError("LinkedList ll_prepend function not yet implemented")


def ll_insert(l: LinkedList, item: int, next_to: Cell) -> Cell:
    raise NotImplementedError("LinkedList ll_insert function not yet implemented")


def ll_remove(l: LinkedList, cell: Cell) -> int:
    raise NotImplementedError("LinkedList ll_remove function not yet implemented")


def ll_extend(l1: LinkedList, l2: LinkedList) -> None:
    raise NotImplementedError("LinkedList ll_extend function not yet implemented")

if __name__=='__main__':

    a : LinkedList = ll_new([1,2,3,4])



    pass