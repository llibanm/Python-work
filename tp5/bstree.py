from tp5.btree import BinaryTree, Node
from tp3.linkedlist import LinkedList
from typing import TypeAlias


BSTree: TypeAlias = BinaryTree


def bst_lookup(bst: BSTree, key: int) -> Node | None:
    raise NotImplementedError("bst_lookup function not implemented yet")


def bst_max(bst: BSTree) -> int:
    raise NotImplementedError("bst_max function not implemented yet")


def bst_insert(bst: BSTree, key: int) -> Node:
    raise NotImplementedError("bst_insert function not implemented yet")


def bst_to_list(bst: BSTree) -> LinkedList:
    raise NotImplementedError("bst_to_list function not implemented yet")



def bst_upper(bst: BSTree, key: int) -> int | None:
    raise NotImplementedError("bst_upper function not implemented yet")


def bst_remove(bst: BSTree, key: int) -> BSTree:
    raise NotImplementedError("bst_remove function not implemented yet")


if __name__ == '__main__':
    pass