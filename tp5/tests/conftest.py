import pytest

from tp5.btree import BinaryTree, Node

'''
INPUT_DUP_TREES = [[1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 2, 2, 3, 3, 4, 4],
        [42, 42, None, 42, None, None, None, 42, None, None, None, None, None, None, None, 42, None, None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, 42]]
INPUT_UNIQUE_TREES = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2, 1, 4, 0, None, 3, 5],
              [1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5, None, None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, 6],
              [6, 4, 5, 2, 1, 9, 7, 3, 0, 11, 12], [6, 4, 5, 2, None, 9, 7, 3, 0, None, None, 11, 12],
               list(range(2 ** 6 + 1))]
INPUT_TREES = INPUT_DUP_TREES + INPUT_UNIQUE_TREES

EMPTY_TREES = [None, []]
INPUT_TREES_WITH_NULL = EMPTY_TREES + INPUT_TREES

INPUT_ORDERED_TREES = [[1], [1, 1], [2, 1], [1, None, 2], [2, 1, 3],
                       [42, 42, None, 42, None, None, None, 42, None, None, None, None, None, None, None, 42],
                       [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4,
                        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5],
                       [6, 2, 11, 1, 4, 7, 12, None, None, 3, None, None, None, 12, 14],
                       [6, 6, 11, 6, None, 11, 12, 6, None, None, None, 11, None, 12, 14, 6],
                       ]
'''

@pytest.fixture
def empty_bt():
    return BinaryTree()

@pytest.fixture
def root_bt():
    """
    42.
    """
    return BinaryTree(Node(42))

@pytest.fixture
def left_node_bt():
    """
     __42
    1
    """
    return BinaryTree(Node(42, Node(1)))

@pytest.fixture
def right_node_bt():
    """
    1___
       42
    """
    return BinaryTree(Node(1, None, Node(42)))

@pytest.fixture
def right_eq_node_bt():
    """
    42___
       42
    """
    return BinaryTree(Node(42, None, Node(42)))


@pytest.fixture
def left_chain_bt():
    """
           __42
        __3
     __2
    1
    """
    return BinaryTree(Node(42, Node(3, Node(2, Node(1)))))

@pytest.fixture
def right_chain_bt():
    """
    1__
       2__
          3__
             42
    """
    return BinaryTree(Node(1, None, Node(2, None, Node(3, None, Node(42)))))

@pytest.fixture
def alternate_chain_bt():
    """
        __42
       1__
         42
    """
    return BinaryTree(Node(42, Node(1, None, Node(42))))

@pytest.fixture
def bt6():
    """
        __2__
     __1    __4__
    0       3   5
    """
    return BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5))))

@pytest.fixture
def bt6_bis():
    """
        __2__
     __1    __4__
    0       3  __5
               1
    """
    return BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5,Node(1)))))


@pytest.fixture
def bt7():
    """
        ___42___
      33___    11__
         __7__     5
        7     1
    """
    return BinaryTree(Node(42, Node(33, None, Node(7, Node(7), Node(1))), Node(11, None, Node(5))))

@pytest.fixture
def bt10():
    """
        _____6_____
     __2___     __11___
    1   __4    7   ___12___
       3          12      14
    """
    return BinaryTree(Node(6, Node(2, Node(1), Node(4, Node(3))), Node(11, Node(7), Node(12, Node(12), Node(14)))))


@pytest.fixture
def bt11():
    """
        _____6_____
     __2___     __11___
    1   __4    7   ___12___
       3       ___12      14
              42
    """
    return BinaryTree(Node(6, Node(2, Node(1), Node(4, Node(3))),
                           Node(11, Node(7), Node(12, Node(12, Node(42)), Node(14)))))



@pytest.fixture
def empty_tree():
    return []

@pytest.fixture
def null_tree():
    return None

@pytest.fixture
def root_tree():
    return [42]

@pytest.fixture
def left_node_tree():
    return [42, 1]

@pytest.fixture
def right_node_tree():
    return [1, None, 42]

@pytest.fixture
def left_chain_tree():
    return [42, 3, None,
            2, None, None, None,
            1]

@pytest.fixture
def right_chain_tree():
    return [1,
            None, 2,
            None, None, None, 3,
            None, None, None, None, None, None, None, 42]

@pytest.fixture
def tree6():
    return [2, 1, 4, 0, None, 3, 5]

@pytest.fixture
def tree7():
    return [42,
            33, 11,
            None, 7, None, 5,
            None, None, 7, 1]

@pytest.fixture
def tree10():
    return [6,
            2, 11,
            1, 4, 7, 12,
            None, None, 3, None, None, None, 12, 14]

@pytest.fixture
def tree11():
    return [6,
            2, 11,
            1, 4, 7, 12,
            None, None, 3, None, None, None, 12, 14,
            None, None, None, None, None, None, None, None, None, None, None, None, 42]