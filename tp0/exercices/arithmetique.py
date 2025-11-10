import random
import pytest

def val_absolue(n:int)->int:
    if n < 0:
        n= n - (n)*2
    return n 

def odd_number(n:int)->bool:
    return n%2==0

def produit_modulo(m:int,n:int,p:int)->int:
    return (n*p)%m

def division(k:int,n:int)->int:
    return n//k

random.seed

#def test_1_val_ablsolue():
#    assert val_absolue(random.randint(-99,99))

#def test_2_val_ablsolue():
#    assert val_absolue(random.randint(-99,99))

#def test_3_val_ablsolue():
#    assert val_absolue(random.randint(-99,99))

"""
@pytest.mark.parametrize("arg,expected",[(-3,3),(+3,3),(-10,10),(4,4)])
def test_val_absolue(arg,expected):
    assert val_absolue(arg) == expected
"""

# pour executer la fct en haut on fait pytest tp0/exercices/arithmetique.py 


@pytest.mark.parametrize("arg,expected",[ (3,False) , (4,True) , (5,False) , (6,True) , (7,False)  ])
def test_odd_number(arg,expected):
    assert odd_number(arg) == expected


@pytest.fixture # m
def forty_two() -> int:
    return 42







#@pytest.mark.parametrize
#def test_produit_modulo(forty_two,arg*forty_two,expected):
   
if __name__=='__main__':

    """
    test_1_val_ablsolue()
    test_2_val_ablsolue()
    test_3_val_ablsolue()
    """    
    odd_number(3)

   

    pass