from tp1.fibo import fibo , fibo_norec, fibo_term
import pytest



###################################
### Test cases : (n, expected fibo(n))
###################################
FIBO_CASES_SMALL = list(zip(range(15), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]))

FIBO_CASES_LARGE = [(20, 6765),
                    (30, 832040),
                    (42, 267914296),
                    (100, 354224848179261915075)]

FIBO_CASES_ALL = FIBO_CASES_SMALL + FIBO_CASES_LARGE

###################################
### Tests
###################################

@pytest.mark.parametrize(('n', 'expected'), FIBO_CASES_SMALL)
def test_fibo(n, expected):
    assert fibo(n) == expected


@pytest.mark.parametrize(('n', 'expected'), FIBO_CASES_ALL)
def test_fibo_norec(n, expected):
    assert fibo_norec(n) == expected


@pytest.mark.parametrize(('n', 'expected'), FIBO_CASES_ALL)
def test_fibo_term(n, expected):
    assert fibo_term(n) == expected
