import pytest
from tp4.stupidsort import stupidsort
from tp4.insertionsort import insertionsort
from tp4.quicksort import quicksort, quicksort_alt
from tp4.countingsort import countingsort

import random

##################################
### Constants /!\ DO NOT TOUCH /!\
##################################

SMALL_INPUT_LISTS = [[], [42], [42] * 100, list(range(7)), list(range(6, -1, -1)), random.choices(range(101), k=7)]
MEDIUM_INPUT_LISTS = [  list(range(42)),
                        list(range(41, -1, -1)),
                        random.choices(range(101), k=10),
                        random.choices(range(101), k=100),
                        random.choices(range(101), k=1_000)]

###################################
### Fixture definitions
###################################

# workaround to return multiple values from a fixture
# request is itself a built-in fixture
# waiting for pytest to allow fixture as parameters
@pytest.fixture(params=SMALL_INPUT_LISTS + MEDIUM_INPUT_LISTS)
def any_seq(request):
    return request.param


@pytest.fixture(params=SMALL_INPUT_LISTS)
def small_seq(request):
    return request.param



###################################
### Tests
###################################

def test_stupidsort(small_seq):
    seq = small_seq[:]        # copy to prevent from modifying the original list
    assert stupidsort(seq) == sorted(seq)


def test_insertionsort(any_seq):
    seq = any_seq[:]
    assert insertionsort(seq) == sorted(seq)


def test_quicksort(any_seq):
    seq = any_seq[:]
    assert quicksort(seq) == sorted(seq)


def test_quicksort_alt(any_seq):
    seq = any_seq[:]
    assert quicksort_alt(seq) == sorted(seq)


def test_countingsort(any_seq):
    seq = any_seq[:]
    assert countingsort(seq) == sorted(seq)

