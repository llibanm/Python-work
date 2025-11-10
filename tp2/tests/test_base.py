import pytest

# functions to test
from tp2.base import mode, cumulative_sum#, duplicate_elimination #, reset_high

# dependencies
from tp2.util import list_to_array, random_array, array_to_list


###########
# fixtures
###########

@pytest.fixture
def random_tab():
    return random_array(1_000, 0, 42)


@pytest.mark.parametrize("tab, expected", [ ([0], 0),
                                            ([0, 1], 0),
                                            ([0, 0, 1], 0),
                                            ([1, 0, 0], 0),
                                            ([1, 0, 0, 1, 0], 0),
                                            ([1, 0, 1, 0, 1, 0, 0, 42], 0),
                                            ([0] * 1_000, 0)])
def test_mode(tab, expected):
    assert mode(list_to_array(tab)) == expected


def test_mode_random(random_tab):
    import statistics
    assert mode(random_tab) == statistics.mode(array_to_list(random_tab))

'''
@pytest.mark.parametrize("l, threshold", [ ([], 1),
                                             ([1], 42),
                                             ([42], 1),
                                             ([0, 42, 1], 1),
                                             ([42] * 10, 33),
                                             (list(range(101)), 42),
                                             (list(reversed(range(101))), 42)])
def test_reset_high(l, threshold):
    tab = to_array(l)
    reset_high(tab, threshold)
    assert list(tab) == [e if e <= threshold else 0 for e in tab]


@pytest.mark.parametrize("threshold", [0, 1, 10, 20, 33, 42])
def test_reset_high_random(random_array, threshold):
    tab = to_array(list(random_array)) # ugly copy!
    reset_high(tab, threshold)
    assert list(tab) == [e if e <= threshold else 0 for e in tab]
'''

@pytest.mark.parametrize("l", [ [],
                                [0],
                                [0, 0],
                                [0, 1, 0],
                                list(range(42)),
                                [42] * 42,
                                list(range(42)) + [42] * 42,
                                [42] * 42 + list(range(42)),
                                list(range(42)) + list(range(42))])
def test_cumulative_sum(l):
    cs = cumulative_sum(list_to_array(l))
    assert array_to_list(cs) == l if len(l) <= 1 else [sum(l[:i]) for i in range(len(l))]

"""
@pytest.mark.parametrize("l", [ [],
                                [0],
                                [0, 0],
                                [0, 1, 0],
                                list(range(42)),
                                [42] * 42,
                                list(range(42)) + [42] * 42,
                                [42] * 42 + list(range(42)),
                                list(range(42)) + list(range(42))])
def test_duplicate_elimination(l):
    tab = duplicate_elimination(list_to_array(l))
    assert array_to_list(tab) == list(dict.fromkeys(l))  # dict preserves insertion order (not set)...


def test_duplicate_elimination_random(random_tab):
    tab = duplicate_elimination(random_tab)
    assert array_to_list(tab) == list(dict.fromkeys(array_to_list(random_tab)))
    """