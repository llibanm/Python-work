import sys

def get_arg():
    if len(sys.argv) <= 1:
        print("where expression ????")
        return -1
    
    return sys.argv[1]

def eval_from_str(expr : str) -> int:

    if expr == "":
        print("empty list")
        return -1

    list_expr : list = []

    pick_variable : str = ""

    for i in range(len(expr)):

        if expr[i] >= "0" and expr[i] <= "9":
            pick_variable += expr[i]

        if expr[i] == "+" or expr[i] == "-" or expr[i] == "*" or expr[i] == "/" or expr[i] == "%":
            list_expr.append(pick_variable)
                


    print(list_expr)
    return 0




if __name__=="__main__":

    eval_from_str("2 + 3")

    pass