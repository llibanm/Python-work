import pytest

import random
import string

DELTA_SIZES = [0, 1, 9, 99]

# random letter lists
CHAR_LISTS = [['a'], [''.join(random.choices(string.ascii_lowercase, k=50)) for _ in range(6)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(10)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(100)]]

CHAR_LISTS2 = [['a'], [''.join(random.choices(string.ascii_lowercase, k=50)) for _ in range(6)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(10)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(100)]]
for i, letter_list in enumerate(CHAR_LISTS):
    CHAR_LISTS[i] = list(set(letter_list))

for i, letter_list2 in enumerate(CHAR_LISTS2):
    CHAR_LISTS2[i] = list(set(letter_list2))


@pytest.fixture(params=DELTA_SIZES)
def dsize(request):
    return request.param


@pytest.fixture(params=CHAR_LISTS)
def char_list(request):
    return request.param


@pytest.fixture(params=CHAR_LISTS2)
def char_list2(request):
    return request.param

