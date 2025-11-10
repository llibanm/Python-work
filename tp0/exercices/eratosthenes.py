import math

def divisible(n,d)-> bool:
    return n % d == 0

def sieve_of_eratosthenes(N:int) -> list[int]:
    
    res :list[int] = []
    for i in range(2,N+1):
        res.append(i)

    #print(res)

    count :int  = 2

    length = (len(res))
    #print(length)

    while(count * count <=N):
        i = 0
        while(i < length):
         #   print(i)
         #   print(res[i])

            if ( res[i] != count):

                if (res[i] % count == 0) :
                    res.pop(i)
                    length = length -1
                    #break
            i+=1        
                    
        #print(res)            
        count+=1                


    return res

if __name__=='__main__':
    print(sieve_of_eratosthenes(100))
    pass