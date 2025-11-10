import pytest

from tp3.linkedlist import Cell, LinkedList, ll_new, ll_is_empty, ll_len, ll_head, ll_tail, ll_insert,\
    ll_prepend, ll_append, ll_iter, ll_str, ll_lookup, ll_cell_at, ll_remove, ll_extend


# Test class definition
class TestLList:

    def test_linked_list_struct(self):
        try:
            LinkedList()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True


# Test ll_new empty
class TestNewIsEmpty:

    def test_linked_list_empty(self):
        assert isinstance(ll_new(), LinkedList)

    def test_ll_is_empty(self):
        assert ll_is_empty(ll_new()) is True


# Test ll_len, ll_head, ll_tail on empty list only (see TestAppend for the regular cases)
class TestHeadTailEmpty:

    def test_ll_head_fails_empty(self):
        ll = ll_new()
        pytest.raises(IndexError, ll_head, ll)

    def test_ll_tail_fails_empty(self):
        ll = ll_new()
        pytest.raises(IndexError, ll_tail, ll)


# Test ll_append
class TestAppend:

    def test_append(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            cells.append(ll_append(ll, e))
            assert ll_tail(ll) is cells[-1]
            # assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(e == c.item  for e, c in zip(input_list, cells))

    def test_is_empty_(self, input_list):
        ll = ll_new()
        for e in input_list:
            ll_append(ll, e)
            assert not ll_is_empty(ll)

    def test_head(self, input_list):
        ll = ll_new()
        for e in input_list:
            ll_append(ll, e)
            assert ll_head(ll).item == input_list[0]

    def test_tail(self, input_list):
        ll = ll_new()
        for i, e in enumerate(input_list):
            ll_append(ll, e)
            assert ll_tail(ll).item == input_list[i]


# Test ll_new with parameters
class TestNewParam:

    def test_new_empty(self, empty_list):
        ll = ll_new(empty_list)
        assert isinstance(ll, LinkedList)
        assert ll_len(ll) == 0
        assert ll_is_empty(ll)

    def test_new(self, input_list):
        ll = ll_new(input_list)
        assert isinstance(ll, LinkedList)
        assert ll_len(ll) == len(input_list)
        assert not ll_is_empty(ll)
        assert ll_head(ll).item == input_list[0]
        assert ll_tail(ll).item == input_list[-1]



# Test ll_iter
class TestIter:

    def test_iter_empty(self):
        ll = ll_new()
        assert list(ll_iter(ll)) == []

    def test_iter(self, input_list):
        ll = ll_new(input_list)
        assert all(c.item == e for c, e in zip(ll_iter(ll), input_list))

    def test_iter_stop(self, input_list):
        ll = ll_new(input_list)
        ill = ll_iter(ll)
        for _ in range(len(input_list)):
            next(ill)
        with pytest.raises(StopIteration):
            next(ill)

    def test_iter_append(self, input_list):
        ll = ll_new()
        for e in input_list:
            ll_append(ll, e)
        assert all(c.item == e for c, e in zip(ll_iter(ll), input_list))


# Test ll_reversed_iter
class TestReversedIter:

    def test_reversed_iter_empty(self):
        ll = ll_new()
        assert list(ll_iter(ll, reverse=True)) == []

    def test_reversed_iter(self, input_list):
        ll = ll_new(input_list)
        assert all(c.item == e for c, e in zip(ll_iter(ll, reverse=True), reversed(input_list)))

    def test_reversed_iter_stop(self, input_list):
        ll = ll_new(input_list)
        rill = ll_iter(ll, reverse=True)
        for _ in range(len(input_list)):
            next(rill)
        with pytest.raises(StopIteration):
            next(rill)


class TestLen:

    def test_ll_len_empty(self):
        ll = ll_new()
        assert ll_len(ll) == 0

    def test_len(self, input_list):
        ll = ll_new()
        for i, e in enumerate(input_list):
            ll_append(ll, e)
            assert ll_len(ll) == i + 1


# Test ll_str
class TestStr:
    def test_str(self, input_list_with_null):
        ll = ll_new(input_list_with_null)
        input_list_with_null = input_list_with_null or []
        assert ll_str(ll) == str(input_list_with_null)


# Test ll_lookup and ll_cell_at
class TestLookupAndCellAt:

    def test_lookup(self, input_list):
        ll = ll_new(input_list)
        for e in input_list:
            found: Cell = ll_lookup(ll, e)
            assert found.item == e
            for c in ll_iter(ll):
                if c is found:
                    break
                assert c.item != e

    @pytest.mark.parametrize("wrong_value", [None, -1, 1_111_111])
    def test_lookup_fails(self, input_list_with_null, wrong_value):
        ll = ll_new(input_list_with_null)
        assert ll_lookup(ll, wrong_value) is None

    def test_cell_at(self, input_list):
        ll = ll_new(input_list)
        assert all(ll_cell_at(ll, i).item == e for i, e in enumerate(input_list))

    @pytest.mark.parametrize("wrong_idx", [None, -1, 1_111_111])
    def test_cell_at_out_of_bounds(self, input_list, wrong_idx):
        ll = ll_new(input_list)
        if wrong_idx is None:
            pytest.raises(IndexError, ll_cell_at, ll, len(input_list))
        else:
            pytest.raises(IndexError, ll_cell_at, ll, wrong_idx)


# Test ll_prepend
class TestPrepend:

    def test_prepend(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            ll_prepend(ll, e)
            cells.append(ll_head(ll))
            assert ll_head(ll).item == e
            assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(c.item == e for e, c in zip(input_list, cells))


# Test ll_insert
class TestInsert:

    def test_insert_next_to_head(self, input_list):
        ll = ll_new([42])
        output_list = [42]
        for i, e in enumerate(input_list):
            c = ll_insert(ll, e, next_to=ll_head(ll))
            output_list.insert(1, e)
            assert c.item == e
            assert ll_len(ll) == i + 2
            assert not ll_is_empty(ll)
        assert all(c.item == e for e, c in zip(output_list, ll_iter(ll)))

    def test_insert_tail(self, input_list):
        ll = ll_new([42])
        for i, e in enumerate(input_list):
            ll_insert(ll, e,  next_to=ll_tail(ll))
            assert ll_tail(ll).item == e
            assert ll_len(ll) == i + 2
            assert not ll_is_empty(ll)
        assert all(c.item == e for e, c in zip([42] + input_list, ll_iter(ll)))


# Test ll_remove
class TestRemove:

    def test_remove(self, input_list_with_null):
        import random
        ll = ll_new(input_list_with_null)
        in_l = input_list_with_null or []
        for max_p in reversed(range(len(in_l))):
            p: int = random.randint(0, max_p)
            ll_remove(ll, ll_cell_at(ll, p))
            in_l = in_l[:p] + in_l[p + 1:]
            assert all(c.item == e for c, e in zip(ll_iter(ll), in_l))
        assert ll_len(ll) == 0
        assert ll_is_empty(ll)


# Test ll_extend
class TestExtend:

    def test_extend(self, input_list_with_null, input_list):
        l1 = ll_new(input_list_with_null)
        in_l1 = input_list_with_null or []
        l2 = ll_new(input_list)
        ll_extend(l1, l2)
        assert ll_len(l1) == len(in_l1) + len(input_list)
        assert ll_len(l2) == len(input_list)
        assert all(c.item == e for c, e in zip(ll_iter(l1), in_l1 + input_list))
        assert all(c.item == e for c, e in zip(ll_iter(l2), input_list))
