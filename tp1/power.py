def power(a : int, n : int) -> int :

    if n == 0:
         return 1

    res : int 

    if n % 2 == 1:
          
            half =  power(a,n//2)
            res  = half * half * a

    else:
            half = power(a,n//2)
            res = half *  half 

    return res     


def superpower(a : int , n : int ) -> int :
      
      if n == 0:
            return 1
      if a == 1:
            return 1
      
      res : int 

      if n % 2 == 1:
            half =  power(a,n//2 +1)
            res  = half * (a**(n//2))
      else :
            half = power(a,n//2)
            res = half *  half 

      return res         

if __name__=='__main__':

    print(power(42**2,2))

    pass