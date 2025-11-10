import pytest
import random
'''
Share fixtures across multiple test files
'''


##################################
### Constants
##################################
DELTA_SIZES = [0, 1, 9, 99]
INPUT_LISTS = [[42], [42] * 10,
               list(range(1, 6)),
               random.choices(range(101), k=10),
               random.choices(range(101), k=100)]
EMPTY_LISTS = [None, []]


###################################
### Fixture definitions
###################################

@pytest.fixture
def random_list_of_10():
    return random.choices(range(101), k=10)


# workaround to return multiple values from a fixture
# request is itself a built-in fixture
# waiting for pytest to allow fixture as parameters
@pytest.fixture(params=INPUT_LISTS)
def input_list(request):
    random.seed(42)
    return request.param


# same workaround as above
@pytest.fixture(params=DELTA_SIZES)
def dsize(request):
    return request.param


@pytest.fixture(params=EMPTY_LISTS)
def empty_list(request):
    return request.param


@pytest.fixture(params=EMPTY_LISTS + INPUT_LISTS)
def input_list_with_null(request):
    return request.param
