from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator


@dataclass
class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children,
    which are referred to as the left child and the right child.

    The BinaryTree class is a dataclass with a single field, root, which is a reference to the root node of the tree.

    The Node class is a nested dataclass with three fields: key, left, and right.
    The key field is an integer that stores the value of the node.
    The left and right fields are references to the left and right children of the node, respectively.

    Example:
        >>> bt = BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5))))
    """
    root: Node | None = None


@dataclass
class Node:
    key: int
    left: Node | None = None       # "Or None" for terminal nodes
    right: Node | None = None



def bt_is_empty(bt: BinaryTree) -> bool:
    #raise NotImplementedError("bt_is_empty function not implemented yet")
    return bt.root == None


def bt_root(bt: BinaryTree) -> Node:
    #raise NotImplementedError("bt_root function not implemented yet")

    if bt.root == None:
        raise ValueError("Error : Root is empty")
    
    return bt.root


def bt_iter_dfs(n: Node) -> Iterator[Node]:
    #raise NotImplementedError("n_iter_dfs function not implemented yet")

    if n == None:
        return

    if n.left == None and n.right == None:
        yield n

    elif n.right == None and n.left != None:
        yield from bt_iter_dfs(n.left)    
        #yield n.left
        yield n

    elif n.right != None and n.left == None:
        yield n
        yield from bt_iter_dfs(n.right)
        #yield n.right

    elif n.right != None and n.left != None:
        yield from bt_iter_dfs(n.left)          
        #yield n.left
        yield n
        #yield n.right
        yield from bt_iter_dfs(n.right)

def bt_iter_bfs(n: Node) -> Iterator[Node]:
    #raise NotImplementedError("n_iter_bfs function not implemented yet")

    if n == None:
        return
    
    pile = [n]

    while pile :

        tmp = pile.pop(0)

        yield tmp 

        if tmp.left is not None:
            pile.append(tmp.left)
        if tmp.right is not None:
            pile.append(tmp.right)    

    



def bt_height(bt: BinaryTree) -> int:
    raise NotImplementedError("bt_height function not implemented yet")


def bt_size(bt: BinaryTree) -> int:
    raise NotImplementedError("bt_size function not implemented yet")


def bt_str(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_str function not implemented yet")


def bt_new(nodes: list[int | None] | None = None) -> BinaryTree:
    raise NotImplementedError("bt_new function not implemented yet")


def bt_is_bst(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_bst function not implemented yet")


def bt_is_heap(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_heap function not implemented yet")


def bt_lca(bt: BinaryTree, a: int, b: int) -> int:
    raise NotImplementedError("bt_lca function not implemented yet")


def bt_prettystr(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_prettystr function not implemented yet")


def lol()->Iterator[int]:
    yield 3
    yield 4

if __name__ == '__main__':
    a = BinaryTree(Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))

    c = bt_iter_bfs(bt_root(a))

    for i in c :
        print(i.key)

    pass    