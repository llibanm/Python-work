from dataclasses import dataclass
from typing import TypeAlias
from btree import BinaryTree,Node

AST : TypeAlias = BinaryTree

Operators = {
    '+':0,
    '-':1,
    '*':2,
    '/':3
}


def check_operator(op:int) -> bool:

    for key,val in Operators.items():
        if op == val:
            return True
        
    return False    


def eval_ast_aux_rec(ast:Node|None) ->float:

    if ast == None :
        return 0   
    

    
    if ast.right == None and ast.left == None:
     
        return float(ast.key)

    res : float = 0

    match ast.key:
        
        case 0: 
           res = eval_ast_aux_rec(ast.left) + eval_ast_aux_rec(ast.right)
        
        case 1:
            res =  eval_ast_aux_rec(ast.left) - eval_ast_aux_rec(ast.right)
        
        case 2:
            res =  eval_ast_aux_rec(ast.left) * eval_ast_aux_rec(ast.right)

        case 3:


            if eval_ast_aux_rec(ast.right) == 0:
                raise ZeroDivisionError()
            res =  eval_ast_aux_rec(ast.left) / eval_ast_aux_rec(ast.right)    

        case _:
            raise ValueError("error: value unknown")    
    

    return res

def eval_ast(ast: AST) -> float:

    if ast == None : # 1er cas, l'arbre est vide
        raise ValueError("AST empy") 

    root  = ast.root

    return eval_ast_aux_rec(root)

def exp_to_ast(tokens: list[str]) -> AST:

    new_ast : AST

    if tokens == []:
        return AST(None)
    
    if len(tokens) % 2 != 0:
        return AST(None)

    def exp_to_ast_aux(tokens: list[str]) -> Node:
        
        first_element = tokens.pop()

        if not Operators[first_element]:
            



def create_ast_example() -> AST:
    
    """
    Crée l'AST de l'expression: (4 - 2) + (3 * 5)
    En notation préfixée: (+ (- 4 2) (* 3 5))
    
    Structure de l'arbre:
           +
          / \
         -   *
        / | / \
       4  2 3  5
    
    Returns:
        L'arbre de syntaxe abstraite correspondant
    """

    four = Node(4)
    two = Node(2)

    three = Node(3)
    five = Node(5)

    minus = Node(
        Operators['-'],
        four,
        two
    )

    times = Node(
        Operators['*'],
        three,
        five
    )

    plus = Node(
        Operators['+'],
        minus,
        times
    )

    return BinaryTree(plus)

if __name__=='__main__':

    

    a = create_ast_example()
    print(eval_ast(a))
    """    print(Operators['+'])
    print(Operators['-'])
    print(Operators['*'])
    print(Operators['/'])"""


    pass