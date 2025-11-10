# Exercise 10

def digit_3(n:int)->bool:
    if n >= 100 and n <= 999:
        return True
    else:
        return False
    
def lessThan_300(n:int)->bool:
    if n < 300:
        return True
    else:
        return False

def isEven(n:int)->bool:
    if n % 2 == 0:
        return True
    else:
        return False

def has_two_identical_digits(n: int) -> bool:
    s = str(n)
    return len(set(s)) < len(s) # set(s) is the set of distinct characters in s
                                # if there are two identical digits, the length of set(s) is less than the length of s

def has_sum_of_digit_equal_seven(n:int)->bool:
    s = str(n)
    sum_digit = 0
    for digit in s:
        sum_digit += int(digit) # convert the character digit to an integer and add it to sum_digit
    if sum_digit == 7:          # if the sum of the digits is equal to 7 return True
        return True
    else:
        return False
                                    

##print(f"Test 1 :",digit_3(999))  # return True
##print(f"Test 2 :",lessThan_300(99)) # return True
##print(f"Test 3 :",isEven(42)) # return True
##print(f"Test 4 :",has_two_identical_digits(1234567891)) #return True
##print(f"Test 5 :",has_sum_of_digit_equal_seven(123)) # return false
  
def mystery_number(n:int)->bool:
    return digit_3(n) and lessThan_300(n) and isEven(n) and has_two_identical_digits(n) and has_sum_of_digit_equal_seven(n)


# Exercise 11

def even_first_odd_last_list(l:list[int])->list[int]:
    res=[]
    len_res_even=0
    len_res_odd=0
    for i in range(len(l)-1):
        if(l[i]%2==0):
            res.insert(len_res_even,l[i])
            len_res_even+=1
        else: 
            res.append(l[i])
            len_res_odd+=1 
    return res

#print(even_first_odd_last_list([123,23,123452,9675,3518,222]))


def check_if_odd(n:int)->bool:
    if n % 2 != 0:
        return True
    else:
        return False

def check_if_even(n:int)->bool:
    if n % 2 == 0:
        return True
    else:
        return False    




       