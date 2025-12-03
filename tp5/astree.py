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


def eval_ast(ast: AST) -> float:

    if ast == None or ast.root == None:
        raise ValueError("AST empy") 

    root :  Node = ast.root

    pass

def create_ast_example() -> AST:
    """
    Crée l'AST de l'expression: (4 - 2) + (3 * 5)
    En notation préfixée: (+ (- 4 2) (* 3 5))
    
    Structure de l'arbre:
           +
          / \
         -   *
        / \ / \
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

    pass