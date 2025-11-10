
def text():
    data : str = ""
    list_str : list[str] 
    res : str = ""


    with open('../data/online_inventaire_prevert.txt','r') as input_file:
        data = input_file.read()
        list_str = data.split(';')

        for i in range(len(list_str)):
            if list_str[i] == "" :
                res += list_str[i] + '\n'
            else :
                res += str(i) + ' ' + list_str[i] + '\n'    
    return res        


#a = "liban,yonis".split(',')

#b : str = a[0] + '\n'
#b += a[1] + '\n'
#print(  b )

if __name__ == '__main__':
    print( text() )
        