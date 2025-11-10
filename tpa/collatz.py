def collatz(u0,n):
    assert u0 >= 0 and n >= 0 # préconditions toujours respectées
    u = u0
    for i in range(n):
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3 * u + 1
    return u


#programme principal

#print("Suite de Collatz") 
#seed = 135
#for i in range(42):
#    print(f" u_{i}={collatz(seed,i)}") # Pourquoi assert n >= 10  si c'est pour un i in rage(42) ?

##print(f" u_42={collatz(seed,42)}")


def collatz_series(u0,N):
    res = [u0]
    for i in range(N):
        if u0 % 2 == 0:
            u0 = u0 // 2
            res.append(u0)
        else:
            u0 = 3 * u0 + 1
            res.append(u0)
    return res

##print(f"Suite de Collatz complète pour {seed} sur 10 itérations : {collatz_series(seed,10)}")

def collatz_lifetime(seed):
    count = 0
    equal_to_one = 1
    while seed != equal_to_one:
        if seed %2 == 0:
            seed = seed // 2
            count += 1
        else:
            seed = 3 * seed + 1
            count += 1        
    return count

##print(f"La durée de vie de la suite de Collatz pour {seed} est : {collatz_lifetime(seed)}")            
    

def collatz_altitude(seed):

    max_value = seed
    equal_to_one = 1 # end condition

    while seed != equal_to_one:
        if seed %2 == 0:
            seed = seed // 2

            if seed > max_value:
                max_value = seed
            else:
                pass    

        else:
            seed = 3 * seed + 1

            if seed > max_value:
                max_value = seed
            else:
                pass   

    #print(seed)
    return max_value


#print(f"L'altitude de la suite de Collatz pour {seed} est : {collatz_altitude(seed)}")               


#def collatz_lifetime(seed):
#   return 2

#def collatz_series(seed,index):
#    return [seed,1]

#def collatz_altitude(seed):
#    return 1


# Exercice 13

def Cesar_encoding(m,key):
    assert key <= 26
    new_m=""
    for i in range(len(m)):
        #new_m+= chr( ord( m[i] )+key )

        tmp = ord( m[i] )
        print(ord(m[i]))

        if tmp + key > 122:
            tmp = 97 + (key-1)
        else :
            tmp += key 

        print(tmp)    

        new_m+= chr(tmp)    
        

    return new_m

#print(Cesar_encoding("bonjour",6))

# Exercice 14

#print(1+2+3+4+5+6+7+9) # normally 45 but 8 is missing so its 37
#print(45-37) # give us 8

def sudoku_line(l):

    count = 0
    index_missing = 0
    
    for i in range(len(l)):
    
        print(count)
        
        if(l[i]) == -1:
            index_missing = i
        else :
            count+= l[i]

    return (index_missing,45-count)

line = [3, 2, 8, -1, 5, 9, 7, 1, 6]
#print(sudoku_line(line))


# Exercice 15

def physical_distancing(seats):
    
    difference_of_index = 0
    i_first = None
    i_seccond = None
    size_of_diff = 0

    size_of_diff_max = 0
    difference_of_index_res = 0
    l = []

    for i in range(len(seats)):

        if seats[i] == 0: # seat with 0
            pass

        else : # seat with 1 
            
            if i_first == None : # i_first wasn't up to date

                i_first = i
            
            else :
                i_seccond = i # i_second wasn't up to date

                difference_of_index = (i_seccond + i_first) //2
                
                size_of_diff = i_seccond - i_first -1

                if size_of_diff_max < size_of_diff:
                    size_of_diff_max = size_of_diff
                    difference_of_index_res = difference_of_index

                l.append((difference_of_index,i_first,i_seccond,size_of_diff))



                i_first = i_seccond 
                i_seccond= None # after the operation we set it back to None 
                pass    
    print(difference_of_index_res)        
        

   
                
        

seats = [0, 1, 0, 0, 1, 0, 0, 0, 1]     #6
seats_2 = [1, 0, 0, 0, 0, 0, 0, 0, 1]   #4
seats_3 = [1,0,1,0,1,0,1,0,1,0] #1

#physical_distancing(seats_3)

#print(7//2)

# TP fini

if __name__ == '__main__':
    print(collatz(132,42))
    pass     
        





            


    

