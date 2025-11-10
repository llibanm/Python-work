numbers: list[int] = list(range(1_000)) #list of numbers from 0 to 999

#for i in range(len(numbers)-1):
#    if not bool(numbers[i] % 2):
#        del numbers[i] 
#    else:    
#       numbers[i] = numbers[i] * i

#print(numbers) 

##correction

llen = len(numbers)-1
i = 0

while(i <= llen):
    if not bool(numbers[i] % 2):
        del numbers[i]
        llen -= 1
    else:
        numbers[i] = numbers[i] * i
        i += 1
    

print(numbers)

