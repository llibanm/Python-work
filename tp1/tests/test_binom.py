from tp1.binom import binom
import pytest

#############################################
### Test cases : (n, k, expected binom(n, k))
#############################################
BINOM_CASES_SMALL = [(42, 0, 1),
            (42, 42, 1),
            (5, 3, 10),
            (10, 0, 1),
            (10, 1, 10),
            (10, 2, 45),
            (10, 3, 120),
            (10, 4, 210),
            (10, 5, 252),
            (10, 6, 210),
            (10, 7, 120),
            (10, 8, 45),
            (10, 9, 10),
            (10, 10, 1),
            (42, 1, 42)]

BINOM_CASES_LARGE = [(42, 10, 1471442973),
            (42, 21, 538257874440),
            (42, 31, 4280561376),
            (100, 50, 100891344545564193334812497256)]


###################################
### Tests
### mark the tests with the correct decorator
###################################

@pytest.mark.parametrize(('n', 'k', 'expected'), BINOM_CASES_SMALL)
def test_binom(n, k, expected):
    assert binom(n, k) == expected


@pytest.mark.parametrize(('n', 'k', 'expected'), BINOM_CASES_SMALL + BINOM_CASES_LARGE)
def test_binom_memo(n, k, expected):
    assert binom(n, k) == expected