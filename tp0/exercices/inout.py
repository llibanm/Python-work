import sys
import argparse

def input_nums_from_cli() -> list[int]:

    catch_int_list : list[int] = []
    res : list[int] = [0]
    sum_boolean : bool = False


    for i in range(len(sys.argv)):
       

       if i == 0:
          pass

       elif sys.argv[i] == '--sum':
           sum_boolean = True
       else :
           catch_int_list.append(int(sys.argv[i]))   
    

    if sum_boolean == True:
        for i in range(len(catch_int_list)):
            res[0] += catch_int_list[i]
              
    else: 
        res = catch_int_list
    return res    


def input_nums_from_cli2_help():
    help = "usage: python -m tp0.inout [--help] [--sum] [NOMBRE ...]\n"+ "Collecte les nombres passés en ligne de commande\n" + "arguments:\n" + "NOMBRE série de nombres à collecter\n" + "options:\n" + "--help affiche ce message d'aide et termine\n"+"--sum réalise la somme des nombres\n"
    return help

def input_nums_from_cli2_file(filepath:str):
    data : str
    content : list[str]
    res : list[int] = []

    with open('../data/numbers.txt','r') as input_file:
        data = input_file.read()
        content = data.split('\n')

        for i in range(len(content)):
            try:
                res.append( int( content[i]  ) )
            except ValueError:
                pass
    return res            



def input_nums_from_cli2() -> list[int]: # gére les erreurs

    catch_int_list : list[int] = []
    res : list[int] = [0]
    
    sum_boolean : bool = False
    file_boolean : bool = False
    arg :str =""
    
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--file',help='Nom du fichier')
    #args = parser.parse_args()

    

    for i in range(len(sys.argv)):

        if sys.argv[i][:6] == '--file':
            arg = sys.argv[i][7:]
            file_boolean = True
            

        if sys.argv[i] == '--help':
            print(input_nums_from_cli2_help())
            return []

        if sys.argv[i] == '--sum':
            sum_boolean = True

        else :

            try:
                catch_int_list.append(int(sys.argv[i]))
            except ValueError:
                pass

    if sum_boolean == True:
        for j in range(len(catch_int_list)):
            res[0] += catch_int_list[j]     

    elif file_boolean == True:
        res = input_nums_from_cli2_file(arg)

    else :
        res = catch_int_list         
    return res



if __name__=='__main__':
    print(input_nums_from_cli2())

    #print(sys.argv[1])

   # parser = argparse.ArgumentParser()
   # parser.add_argument('--file',help='Nom du fichier')

   # args = parser.parse_args()
   # a=args._get_args
   # print(type(a))

    pass