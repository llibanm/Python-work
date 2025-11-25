from xml.dom.NodeFilter import NodeFilter

import pytest

from tp5.bstree import bst_lookup, bst_max, bst_insert, bst_to_list, bst_upper, bst_remove

# utilities
from tp5.btree import BinaryTree, Node
from tp3.linkedlist import ll_new, ll_iter, ll_len

"""
Test BSTree functions

Relevant fixtures are empty_bt, root_bt, left_node_bt, right_node_bt, left_chain_bt, right_chain_bt, bt6, bt10.
Trees bt7 and bt11 are not BST.

See conftest.py for the tree structures.
"""

class TestLookup:

    def test_lookup_empty(self, empty_bt):
        assert bst_lookup(empty_bt, 42) is None, "Empty tree should return None"

    def test_lookup_root(self, root_bt):
        assert bst_lookup(root_bt, 42) == root_bt.root

    @pytest.mark.parametrize("key", [1, 43])
    def test_lookup_root_null(self, root_bt, key):
        assert bst_lookup(root_bt, key) is None

    @pytest.mark.parametrize("key", [1, 42])
    def test_lookup_left_node(self, left_node_bt, key):
        assert bst_lookup(left_node_bt, key).key == key

    @pytest.mark.parametrize("key", [0, 22, 43])
    def test_lookup_left_node_null(self, left_node_bt, key):
        assert bst_lookup(left_node_bt, key) is None

    @pytest.mark.parametrize("key", [1, 42])
    def test_lookup_right_node(self, right_node_bt, key):
        assert bst_lookup(right_node_bt, key).key == key

    @pytest.mark.parametrize("key", [0, 22, 43])
    def test_lookup_right_node_null(self, right_node_bt, key):
        assert bst_lookup(right_node_bt, key) is None

    @pytest.mark.parametrize("key", [1, 2, 3, 42])
    def test_lookup_left_chain(self, left_chain_bt, key):
        assert bst_lookup(left_chain_bt, key).key == key

    @pytest.mark.parametrize("key", [0, 22, 43])
    def test_lookup_left_chain_null(self, left_chain_bt, key):
        assert bst_lookup(left_chain_bt, key) is None

    @pytest.mark.parametrize("key", [1, 2, 3, 42])
    def test_lookup_right_chain(self, right_chain_bt, key):
        assert bst_lookup(right_chain_bt, key).key == key

    @pytest.mark.parametrize("key", [0, 22, 43])
    def test_lookup_right_chain_null(self, right_chain_bt, key):
        assert bst_lookup(right_chain_bt, key) is None

    @pytest.mark.parametrize("key", [0, 1, 2, 3, 4, 5])
    def test_lookup_bt6(self, bt6, key):
        assert bst_lookup(bt6, key).key == key

    @pytest.mark.parametrize("key", [-1, 6, 42])
    def test_lookup_bt6_null(self, bt6, key):
        assert bst_lookup(bt6, key) is None

    @pytest.mark.parametrize("key", [1, 2, 3, 4, 6, 7, 11, 12, 14])
    def test_lookup_bt10(self, bt10, key):
        assert bst_lookup(bt10, key).key == key

    @pytest.mark.parametrize("key", [0, 5, 8, 13, 42])
    def test_lookup_bt10_null(self, bt10, key):
        assert bst_lookup(bt10, key) is None


### Test bst_max
class TestMax:

        def test_max_empty_fails(self, empty_bt):
            with pytest.raises(ValueError):
                bst_max(empty_bt), "Empty tree should raise ValueError"

        def test_max_root(self, root_bt):
            assert bst_max(root_bt) == 42

        def test_max_left_node(self, left_node_bt):
            assert bst_max(left_node_bt) == 42

        def test_max_right_node(self, right_node_bt):
            assert bst_max(right_node_bt) == 42

        def test_max_left_chain(self, left_chain_bt):
            assert bst_max(left_chain_bt) == 42

        def test_max_right_chain(self, right_chain_bt):
            assert bst_max(right_chain_bt) == 42

        def test_max_bt6(self, bt6):
            assert bst_max(bt6) == 5

        def test_max_bt10(self, bt10):
            assert bst_max(bt10) == 14



### Test bst_insert
class TestInsert:

    def test_insert_empty(self, empty_bt):
        key = 42
        node = bst_insert(empty_bt, key)
        assert node.key == key, "Should return the inserted node"
        assert empty_bt == BinaryTree(Node(key))

    @pytest.mark.parametrize("key", [33, 42])
    def test_insert_root_left_and_duplicate(self, root_bt, key):
        node = bst_insert(root_bt, key)
        assert node.key == key, "Should return the inserted node"
        assert root_bt == BinaryTree(Node(42, Node(key)))

    def test_insert_root_right(self, root_bt):
        key = 99
        node = bst_insert(root_bt, key)
        assert node.key == key, "Should return the inserted node"
        assert root_bt == BinaryTree(Node(42, None, Node(key)))

    @pytest.mark.parametrize("key", [0, 1])
    def test_insert_left_node_min_and_duplicate(self, left_node_bt, key):
        bst_insert(left_node_bt, key)
        assert left_node_bt == BinaryTree(Node(42, Node(1, Node(key))))

    def test_insert_left_node_max(self, left_node_bt):
        key = 99
        bst_insert(left_node_bt, key)
        assert left_node_bt == BinaryTree(Node(42, Node(1), Node(key)))

    def test_insert_left_node_mid(self, left_node_bt):
        key = 33
        bst_insert(left_node_bt, key)
        assert left_node_bt == BinaryTree(Node(42, Node(1, None, Node(key))))

    def test_insert_left_node_duplicate(self, left_node_bt):
        key = 42
        bst_insert(left_node_bt, key)
        assert left_node_bt == BinaryTree(Node(42, Node(key, Node(1))))

    @pytest.mark.parametrize("key", [0, 1])
    def test_insert_right_node_min_and_duplicate(self, right_node_bt, key):
        bst_insert(right_node_bt, key)
        assert right_node_bt == BinaryTree(Node(1, Node(key), Node(42)))

    def test_insert_right_node_max(self, right_node_bt):
        key = 43
        bst_insert(right_node_bt, key)
        assert right_node_bt == BinaryTree(Node(1, None, Node(42, None, Node(key))))

    @pytest.mark.parametrize("key", [33, 42])
    def test_insert_right_node_mid_and_duplicate(self, right_node_bt, key):
        bst_insert(right_node_bt, key)
        assert right_node_bt == BinaryTree(Node(1, None, Node(42, Node(key))))




### Test bst_to_list
class TestToList:
    """
    Warning: equality check (of List or Cells) may raise a RecursionError with the sentinel node,
    since it introduces a cycle in the chain.
    
    Workaround: check the content of each cell.
    """
    def test_to_list_empty(self, empty_bt):
        llist = bst_to_list(empty_bt)
        it_llist = ll_iter(llist)
        with pytest.raises (StopIteration):
            next(it_llist)

    def test_to_list_root(self, root_bt):
        llist = bst_to_list(root_bt)
        expected_llist = ll_new([42])
        assert ll_len(llist) == 1
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_left_node(self, left_node_bt):
        llist = bst_to_list(left_node_bt)
        expected_llist = ll_new([1, 42])
        assert ll_len(llist) == 2
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_right_node(self, right_node_bt):
        llist = bst_to_list(right_node_bt)
        expected_llist = ll_new([1, 42])
        assert ll_len(llist) == 2
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_left_chain(self, left_chain_bt):
        llist = bst_to_list(left_chain_bt)
        expected_llist = ll_new([1, 2, 3, 42])
        assert ll_len(llist) == 4
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_right_chain(self, right_chain_bt):
        llist = bst_to_list(right_chain_bt)
        expected_llist = ll_new([1, 2, 3, 42])
        assert ll_len(llist) == 4
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_bt6(self, bt6):
        llist = bst_to_list(bt6)
        expected_llist = ll_new([0, 1, 2, 3, 4, 5])
        assert ll_len(llist) == 6
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))

    def test_to_list_bt10(self, bt10):
        llist = bst_to_list(bt10)
        expected_llist = ll_new([1, 2, 3, 4, 6, 7, 11, 12, 12, 14])
        assert ll_len(llist) == 10
        assert all(x.item == y.item for (x, y) in zip(ll_iter(llist), ll_iter(expected_llist)))


### Test bst_upper
class TestUpper:

    def test_upper_empty(self, empty_bt):
        assert bst_upper(empty_bt, 42) is None

    @pytest.mark.parametrize("key", [0, 33, 42])
    def test_upper_root(self, root_bt, key):
        assert bst_upper(root_bt, key) == 42

    @pytest.mark.parametrize("key", [43, 99])
    def test_upper_root_max(self, root_bt, key):
        assert bst_upper(root_bt, 99) is None

    @pytest.mark.parametrize("key, expected", [(0, 1), (1, 1), (33, 42), (42, 42)])
    def test_upper_left_node(self, left_node_bt, key, expected):
        assert bst_upper(left_node_bt, key) == expected

    @pytest.mark.parametrize("key", [43, 99])
    def test_upper_left_node_max(self, left_node_bt, key):
        assert bst_upper(left_node_bt, key) is None

    @pytest.mark.parametrize("key, expected", [(0, 1), (1, 1), (33, 42), (42, 42)])
    def test_upper_right_node(self, right_node_bt, key, expected):
        assert bst_upper(right_node_bt, key) == expected

    @pytest.mark.parametrize("key", [43, 99])
    def test_upper_right_node_max(self, right_node_bt, key):
        assert bst_upper(right_node_bt, key) is None

    @pytest.mark.parametrize("key, expected", [(0, 1), (1, 1), (2, 2), (3, 3), (4, 42), (42, 42)])
    def test_upper_left_chain(self, left_chain_bt, key, expected):
        assert bst_upper(left_chain_bt, key) == expected

    @pytest.mark.parametrize("key", [43, 99])
    def test_upper_left_chain_max(self, left_chain_bt, key):
        assert bst_upper(left_chain_bt, key) is None

    @pytest.mark.parametrize("key, expected", [(0, 1), (1, 1), (2, 2), (3, 3), (4, 42), (42, 42)])
    def test_upper_right_chain(self, right_chain_bt, key, expected):
        assert bst_upper(right_chain_bt, key) == expected

    @pytest.mark.parametrize("key", [43, 99])
    def test_upper_right_chain_max(self, right_chain_bt, key):
        assert bst_upper(right_chain_bt, key) is None

    @pytest.mark.parametrize("key, expected", [(-42, 0), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    def test_upper_bt6(self, bt6, key, expected):
        assert bst_upper(bt6, key) == expected

    @pytest.mark.parametrize("key", [6, 42])
    def test_upper_bt6_max(self, bt6, key):
        assert bst_upper(bt6, key) is None

    @pytest.mark.parametrize("key, expected", [(-42, 1), (0, 1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 6), (6, 6), (7, 7),
                                               (8, 11), (11, 11), (12, 12), (13, 14), (14, 14)])
    def test_upper_bt10(self, bt10, key, expected):
        assert bst_upper(bt10, key) == expected

    @pytest.mark.parametrize("key", [15, 42])
    def test_upper_bt10_max(self, bt10, key):
        assert bst_upper(bt10, key) is None


### Test bst_remove
class TestRemove:
    # TODO: implement tests for bst_remove
    pass
