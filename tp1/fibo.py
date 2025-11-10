#from decorators import trace
import pytest


def fibo(n:int) -> int :
    if n <2:
        return n
    else :
        return fibo(n-1) + fibo(n-2)
    
    

def fibo_norec(n:int)->int:



    if n == 1:
        return 1
    if n == 0 :
        return 0


    count = 2
    a = 0
    b = 1
    tmp = 0
    while count != n+1:
        temp = b 
        b += a 
        a = temp
        count +=1
        
    return b

def fibo_term(n:int) -> int :
  
  if n >= 2:
    return fibo_term_aux(n+1,1,0)
  elif n == 1:
     return 1
  return 0
 
        

#@trace 
def fibo_term_aux(count : int,fn : int, fn_1 :int) -> int:
    if count == 2:
        return fn
    else : 
        return fibo_term_aux(count-1,fn +fn_1,fn)





if __name__=="__main__":
    
   for i in range(2,100):
    print(fibo_term(i))

    # f2 5 fois   
    #
    # 1 + t(n-1) + t(n-2) complexité  
    
    pass