import pytest

#----- fonctions to test -----
from tp2.util import StaticArray, alloc, list_to_array, random_array, nops, reset_nops
# and getitem, setitem, len

def test_alloc_default(array_length):
    assert isinstance(alloc(array_length), StaticArray)


def test_alloc_large_array():
    assert isinstance(alloc(1 << 24), StaticArray)


def test_alloc_fails(array_length):
    with pytest.raises(ValueError):
        alloc(-array_length - 1)


def test_len(array_length):
    t = alloc(array_length)
    assert len(t) == array_length


def test_getitem(array_length):
    t = alloc(array_length)
    assert all(0 == t.__getitem__(i) for i in range(array_length))


def test_getitem_fails(array_length):
    t = alloc(array_length)
    with pytest.raises(IndexError): t.__getitem__(array_length)
    with pytest.raises(IndexError): t.__getitem__(-1)


def test_setitem(array_length):
    t = alloc(array_length)
    for i in range(array_length):
        t.__setitem__(i, i)
    assert all(i == t.__getitem__(i) for i in range(array_length))


def test_setitem_key_fails(array_length):
    t = alloc(array_length)
    with pytest.raises(IndexError): t.__setitem__(array_length, 42)
    with pytest.raises(IndexError): t.__setitem__(-1, 42)


@pytest.mark.parametrize('large_value', [1 << 64, -1 << 64])
def test_setitem_value_fails(array_length, large_value):
    t = alloc(array_length)
    with pytest.raises(OverflowError): t.__setitem__(array_length, large_value)     # whatever the index


def test_list_to_array(input_list_with_null):
    t = list_to_array(input_list_with_null)
    assert len(t) == (len(input_list_with_null) if input_list_with_null is not None else 0)
    assert all(t[i] == input_list_with_null[i] for i in range(len(t)))


@pytest.mark.parametrize("m, a, b", [(0, 0, 0), (1, 0, 0), (42, 0, 0),
                                     (1, 0, 42), (42, 0, 1), (42, 0, 42),
                                     (100_000, 0, 100)])
def test_random_array(m, a, b):
    t = random_array(m, a, b)
    assert len(t) == m
    assert all(a <= t[i] <= b for i in range(m))


def test_array_to_str_length(input_list_with_null):
    t = list_to_array(input_list_with_null)
    l = input_list_with_null if input_list_with_null is not None else []
    for i in range(len(t)):
        t[i] = l[i]
    assert str(t) == str(l)


def test_nops(input_list):
    t = list_to_array(input_list)
    for i in range(10):
        for j in range(len(t)):
            t[j]    # 1 read
            t[j] = 42
            assert nops(t) == {'nread': i*len(t)+j+1, 'nwrite': i*len(t)+j+1}


def test_reset_nops_read(input_list):
    t = list_to_array(input_list)
    for i in range(5):
        reset_nops(t, 'r')
        for j in range(len(t)):
            t[j]
            t[j] = 42
            assert nops(t) == {'nread': j+1, 'nwrite': i*len(t)+j+1}


def test_reset_nops_write(input_list):
    t = list_to_array(input_list)
    for i in range(5):
        reset_nops(t, 'w')
        for j in range(len(t)):
            t[j]
            t[j] = 42
            assert nops(t) == {'nread': i*len(t)+j+1, 'nwrite': j+1}


def test_reset_nops_read_write(input_list):
    t = list_to_array(input_list)
    for i in range(5):
        reset_nops(t, 'rw')
        for j in range(len(t)):
            t[j]
            t[j] = 42
            assert nops(t) == {'nread': j+1, 'nwrite': j+1}


@pytest.mark.parametrize('mode', [42, 'rwr', 'x', True])
def test_reset_nops_fails(input_list, mode):
    t = list_to_array(input_list)
    with pytest.raises(ValueError): reset_nops(t, mode)