def count_digits(n: int, base: int = 10) -> int :

    digits = 0
    var_base = base
    var_n = n
    res = 1
    tmp = 0
    while (var_n >= 1) : 
        tmp = var_n // base 
        if tmp >=1:
            res+=1
        var_n = tmp    
    return res

# for base < 10
def convert_aux_rec(n:int,reste: int,base : int) -> str :

    if n < base :
        return str(n)
    
    return  convert_aux_rec(n//base,0, base)+str(n % base) 


def convert(n : int, base : int) -> str:
    return convert_aux_rec(n,n % base,base)

if __name__=="__main__":

    print( convert(861,5) )

    pass