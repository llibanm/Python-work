import pytest

from tp5.btree import Node, BinaryTree, bt_new, bt_is_empty, bt_root, bt_iter_dfs, bt_iter_bfs, \
    bt_height, bt_size, bt_str, bt_is_bst, bt_is_heap, bt_lca


##############################
### Test data structures
class TestBTree:

    def test_node_type_default(self):
        node = Node(0)
        assert isinstance(node.key, int)
        assert node.left is None
        assert node.right is None

    def test_node_type(self):
        node = Node(0, Node(1), Node(42))
        assert isinstance(node.key, int)
        assert isinstance(node.left, Node)
        assert isinstance(node.right, Node)

    def test_node_struct(self):
        node = Node(0, Node(1), Node(42))
        assert node.key == 0
        assert node.left.key == 1
        assert node.right.key == 42
        assert node.left.left is None
        assert node.left.right is None
        assert node.right.left is None
        assert node.right.right is None

    def test_btree_type_default(self):
        bt = BinaryTree()
        assert bt.root is None

    def test_btree_type(self):
        bt = BinaryTree(Node(42))
        assert isinstance(bt.root, Node)

    def test_btree_struct(self):
        bt = BinaryTree(Node(42))
        assert bt.root.key == 42


##############################
### Test bt_is_empty and bt_root
class TestIsEmptyAndRoot:

    def test_is_empty(self, empty_bt):
        assert bt_is_empty(empty_bt)

    def test_is_not_empty_root(self, root_bt):
        assert not bt_is_empty(root_bt)

    def test_is_not_empty_left_node(self, left_node_bt):
        assert not bt_is_empty(left_node_bt)

    def test_is_not_empty_right_node(self, right_node_bt):
        assert not bt_is_empty(right_node_bt)

    def test_is_not_empty_bt6(self, bt6):
        assert not bt_is_empty(bt6)

    def test_bt_root_fails(self, empty_bt):
        with pytest.raises(ValueError):
            bt_root(empty_bt), "Empty tree should raise a ValueError"

    def test_bt_root_root(self, root_bt):
        assert bt_root(root_bt) is root_bt.root

    def test_bt_root_left_node(self, left_node_bt):
        assert bt_root(left_node_bt) is left_node_bt.root

    def test_bt_root_right_node(self, right_node_bt):
        assert bt_root(right_node_bt) is right_node_bt.root

    def test_bt_root_bt6(self, bt6):
        assert bt_root(bt6) is bt6.root



##############################
### Test bt_iter_dfs
class TestIterDFS:

    def test_bt_iter_dfs_empty(self, empty_bt):
        iter_bt = bt_iter_dfs(empty_bt.root)
        with pytest.raises(StopIteration):
            next(iter_bt)

    def test_bt_iter_dfs_root(self, root_bt):
        assert [n.key for n in bt_iter_dfs(root_bt.root)] == [42]

    def test_bt_iter_dfs_left_node(self, left_node_bt):
        assert [n.key for n in bt_iter_dfs(left_node_bt.root)] == [1, 42]

    def test_bt_iter_dfs_right_node(self, right_node_bt):
        assert [n.key for n in bt_iter_dfs(right_node_bt.root)] == [1, 42]

    def test_bt_iter_dfs_left_chain(self, left_chain_bt):
        assert [n.key for n in bt_iter_dfs(left_chain_bt.root)] == [1, 2, 3, 42]

    def test_bt_iter_dfs_right_chain(self, right_chain_bt):
        assert [n.key for n in bt_iter_dfs(right_chain_bt.root)] == [1, 2, 3, 42]

    def test_bt_iter_dfs_bt6(self, bt6):
        assert [n.key for n in bt_iter_dfs(bt6.root)] == [0, 1, 2, 3, 4, 5]

    def test_bt_iter_dfs_bt7(self, bt7):
        assert [n.key for n in bt_iter_dfs(bt7.root)] == [33, 7, 7, 1, 42, 11, 5]

    def test_bt_iter_dfs_bt10(self, bt10):
        assert [n.key for n in bt_iter_dfs(bt10.root)] == [1, 2, 3, 4, 6, 7, 11, 12, 12, 14]

    def test_bt_iter_dfs_bt11(self, bt11):
        assert [n.key for n in bt_iter_dfs(bt11.root)] == [1, 2, 3, 4, 6, 7, 11, 42, 12, 12, 14]



##############################
### Test bt_iter_bfs
class TestIterBFS:

    def test_bt_iter_bfs_empty(self, empty_bt):
        iter_bt = bt_iter_bfs(empty_bt.root)
        with pytest.raises(StopIteration):
            next(iter_bt)

    def test_bt_iter_bfs_root(self, root_bt):
        assert [n.key for n in bt_iter_bfs(root_bt.root)] == [42]

    def test_bt_iter_bfs_left_node(self, left_node_bt):
        assert [n.key for n in bt_iter_bfs(left_node_bt.root)] == [42, 1]

    def test_bt_iter_bfs_right_node(self, right_node_bt):
        assert [n.key for n in bt_iter_bfs(right_node_bt.root)] == [1, 42]

    def test_bt_iter_bfs_left_chain(self, left_chain_bt):
        assert [n.key for n in bt_iter_bfs(left_chain_bt.root)] == [42, 3, 2, 1]

    def test_bt_iter_bfs_right_chain(self, right_chain_bt):
        assert [n.key for n in bt_iter_bfs(right_chain_bt.root)] == [1, 2, 3, 42]

    def test_bt_iter_bfs_bt6(self, bt6):
        assert [n.key for n in bt_iter_bfs(bt6.root)] == [2, 1, 4, 0, 3, 5]

    def test_bt_iter_bfs_bt7(self, bt7):
        assert [n.key for n in bt_iter_bfs(bt7.root)] == [42, 33, 11, 7, 5, 7, 1]

    def test_bt_iter_bfs_bt10(self, bt10):
        assert [n.key for n in bt_iter_bfs(bt10.root)] == [6, 2, 11, 1, 4, 7, 12, 3, 12, 14]

    def test_bt_iter_bfs_bt11(self, bt11):
        assert [n.key for n in bt_iter_bfs(bt11.root)] == [6, 2, 11, 1, 4, 7, 12, 3, 12, 14, 42]



##############################
### Test bt_height and bt_size
class TestHeightAndSize:

    def test_bt_height_empty(self, empty_bt):
        assert bt_height(empty_bt) == -1

    def test_bt_height_root(self, root_bt):
        assert bt_height(root_bt) == 0

    def test_bt_height_left_node(self, left_node_bt):
        assert bt_height(left_node_bt) == 1

    def test_bt_height_right_node(self, right_node_bt):
        assert bt_height(right_node_bt) == 1

    def test_bt_height_left_chain(self, left_chain_bt):
        assert bt_height(left_chain_bt) == 3

    def test_bt_height_right_chain(self, right_chain_bt):
        assert bt_height(right_chain_bt) == 3

    def test_bt_height_bt6(self, bt6):
        assert bt_height(bt6) == 2

    def test_bt_height_bt7(self, bt7):
        assert bt_height(bt7) == 3

    def test_bt_height_bt10(self, bt10):
        assert bt_height(bt10) == 3

    def test_bt_height_bt11(self, bt11):
        assert bt_height(bt11) == 4

    def test_bt_size_empty(self, empty_bt):
        assert bt_size(empty_bt) == 0

    def test_bt_size_root(self, root_bt):
        assert bt_size(root_bt) == 1

    def test_bt_size_left_node(self, left_node_bt):
        assert bt_size(left_node_bt) == 2

    def test_bt_size_right_node(self, right_node_bt):
        assert bt_size(right_node_bt) == 2

    def test_bt_size_left_chain(self, left_chain_bt):
        assert bt_size(left_chain_bt) == 4

    def test_bt_size_right_chain(self, right_chain_bt):
        assert bt_size(right_chain_bt) == 4

    def test_bt_size_bt6(self, bt6):
        assert bt_size(bt6) == 6

    def test_bt_size_bt7(self, bt7):
        assert bt_size(bt7) == 7

    def test_bt_size_bt10(self, bt10):
        assert bt_size(bt10) == 10

    def test_bt_size_bt11(self, bt11):
        assert bt_size(bt11) == 11



##############################
### Test bt_str
class TestStr:

    def test_bt_str_empty(self, empty_bt):
        assert bt_str(empty_bt) == ""

    def test_bt_str_root(self, root_bt):
        assert bt_str(root_bt) == "42"

    def test_bt_str_left_node(self, left_node_bt):
        assert bt_str(left_node_bt) == "42 (1) ()"

    def test_bt_str_right_node(self, right_node_bt):
        assert bt_str(right_node_bt) == "1 () (42)"

    def test_bt_str_left_chain(self, left_chain_bt):
        assert bt_str(left_chain_bt) == "42 (3 (2 (1) ()) ()) ()"

    def test_bt_str_right_chain(self, right_chain_bt):
        assert bt_str(right_chain_bt) == "1 () (2 () (3 () (42)))"

    def test_bt_str_bt6(self, bt6):
        assert bt_str(bt6) == "2 (1 (0) ()) (4 (3) (5))"

    def test_bt_str_bt7(self, bt7):
        assert bt_str(bt7) == "42 (33 () (7 (7) (1))) (11 () (5))"

    def test_bt_str_bt10(self, bt10):
        assert bt_str(bt10) == "6 (2 (1) (4 (3) ())) (11 (7) (12 (12) (14)))"

    def test_bt_str_bt11(self, bt11):
        assert bt_str(bt11) == "6 (2 (1) (4 (3) ())) (11 (7) (12 (12 (42) ()) (14)))"



##############################
### Test bt_new
class TestNew:

    def test_bt_new_default(self, empty_bt):
        assert bt_new() == empty_bt

    @pytest.mark.parametrize("k", [0, 1, 42, 100])
    def test_bt_new_nulls(self, k, empty_bt):
        assert bt_new([None] * k) == empty_bt

    def test_bt_new_empty_tree(self, empty_tree, empty_bt):
        assert bt_new(empty_tree) == empty_bt

    def test_bt_new_null_tree(self, null_tree, empty_bt):
        assert bt_new(null_tree) == empty_bt

    def test_bt_new_root(self, root_tree, root_bt):
        assert bt_new(root_tree) == root_bt

    def test_bt_new_left_node(self, left_node_tree, left_node_bt):
        assert bt_new(left_node_tree) == left_node_bt

    def test_bt_new_right_node(self, right_node_tree, right_node_bt):
        assert bt_new(right_node_tree) == right_node_bt

    def test_bt_new_left_chain(self, left_chain_tree, left_chain_bt):
        assert bt_new(left_chain_tree) == left_chain_bt

    def test_bt_new_right_chain(self, right_chain_tree, right_chain_bt):
        assert bt_new(right_chain_tree) == right_chain_bt

    def test_bt_new_bt6(self, tree6, bt6):
        assert bt_new(tree6) == bt6

    def test_bt_new_bt7(self, tree7, bt7):
        assert bt_new(tree7) == bt7

    def test_bt_new_bt10(self, tree10, bt10):
        assert bt_new(tree10) == bt10

    def test_bt_new_bt11(self, tree11, bt11):
        assert bt_new(tree11) == bt11



##############################
### Test bt_is_bst
class TestIsBST:

    def test_bt_is_bst_empty(self, empty_bt):
        assert bt_is_bst(empty_bt)

    def test_bt_is_bst_root(self, root_bt):
        assert bt_is_bst(root_bt)

    def test_bt_is_bst_left_node(self, left_node_bt):
        assert bt_is_bst(left_node_bt)

    def test_bt_is_bst_right_node(self, right_node_bt):
        assert bt_is_bst(right_node_bt)

    def test_bt_is_bst_right_eq_node(self, right_eq_node_bt):
        assert not bt_is_bst(right_eq_node_bt)

    def test_bt_is_bst_left_chain(self, left_chain_bt):
        assert bt_is_bst(left_chain_bt)

    def test_bt_is_bst_right_chain(self, right_chain_bt):
        assert bt_is_bst(right_chain_bt)

    def test_bt_is_bst_alternate_chain(self, alternate_chain_bt):
        assert not bt_is_bst(alternate_chain_bt)

    def test_bt_is_bst_bt6(self, bt6):
        assert bt_is_bst(bt6)

    def test_bt_is_bst_bt6_bis(self, bt6_bis):
        assert not bt_is_bst(bt6_bis)

    def test_bt_is_bst_bt7(self, bt7):
        assert not bt_is_bst(bt7)

    def test_bt_is_bst_bt10(self, bt10):
        assert bt_is_bst(bt10)

    def test_bt_is_bst_bt11(self, bt11):
        assert not bt_is_bst(bt11)



##############################
### Test bt_is_heap
class TestIsHeap:

    def test_bt_is_heap_empty(self, empty_bt):
        assert bt_is_heap(empty_bt)

    def test_bt_is_heap_root(self, root_bt):
        assert bt_is_heap(root_bt)

    def test_bt_is_heap_left_node(self, left_node_bt):
        assert bt_is_heap(left_node_bt)

    def test_bt_is_heap_right_node(self, right_node_bt):
        assert not bt_is_heap(right_node_bt)

    def test_bt_is_heap_left_chain(self, left_chain_bt):
        assert bt_is_heap(left_chain_bt)

    def test_bt_is_heap_right_chain(self, right_chain_bt):
        assert not bt_is_heap(right_chain_bt)

    def test_bt_is_heap_bt6(self, bt6):
        assert not bt_is_heap(bt6)

    def test_bt_is_heap_bt7(self, bt7):
        assert bt_is_heap(bt7)

    def test_bt_is_heap_bt10(self, bt10):
        assert not bt_is_heap(bt10)

    def test_bt_is_heap_bt11(self, bt11):
        assert not bt_is_heap(bt11)


##############################
### Test bt_lca
class TestLCA:

    def test_bt_lca_root(self, root_bt):
        assert bt_lca(root_bt, 42, 42) == 42

    @pytest.mark.parametrize(("a", "b", "expected"), [(42, 1, 42), (1, 42, 42), (1, 1, 1)])
    def test_bt_lca_left_node(self, left_node_bt, a, b, expected):
        assert bt_lca(left_node_bt, a, b) == expected

    @pytest.mark.parametrize(("a", "b", "expected"), [(42, 1, 1), (1, 42, 1), (42, 42, 42)])
    def test_bt_lca_right_node(self, right_node_bt, a, b, expected):
         assert bt_lca(right_node_bt, a, b) == expected

    @pytest.mark.parametrize(("a", "b", "expected"), [(1, 3, 3), (3, 1, 3), (2, 42, 42), (1, 42, 42)])
    def test_bt_lca_left_chain(self, left_chain_bt, a, b, expected):
        assert bt_lca(left_chain_bt, a, b) == expected

    @pytest.mark.parametrize(("a", "b", "expected"), [(1, 3, 1), (3, 2, 2), (1, 42, 1), (3, 42, 3)])
    def test_bt_lca_right_chain(self, right_chain_bt, a, b, expected):
        assert bt_lca(right_chain_bt, a, b) == expected

    @pytest.mark.parametrize(("a", "b", "expected"), [(0, 5, 2), (5, 1, 2), (1, 3, 2), (4, 0, 2), (3, 5, 4)])
    def test_bt_lca_bt6(self, bt6, a, b, expected):
        assert bt_lca(bt6, a, b) == expected



##############################
### Test bt_pretty_str
class TestPrettyStr:
    # TODO: implement this test
    pass