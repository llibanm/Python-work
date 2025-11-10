
def input_number_from_kb(prompt: str='Saisir un nombre entier : ') -> int:
    res : int = -1

    try:
        s = input(prompt)
        res  = int(s)
    except ValueError :
        print("Error : not an int")
        
    return res




if __name__ == '__main__':
    print ( input_number_from_kb())
    pass