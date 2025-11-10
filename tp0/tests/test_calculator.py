from tp0.calculator import eval_from_str
import pytest


@pytest.mark.parametrize(('expr', 'expected'), [("344+15", 359),
                                                (" 22 / 432  ", 0),
                                                ("93451*   0", 0),
                                                ("12 %3", 0),
                                                ("7 * 6", 42),
                                                ("1764 / 42", 42),
                                                ("123456789042 - 123456789000", 42)])
def test_eval_from_str(expr, expected):
    assert eval_from_str(expr) == expected


@pytest.mark.parametrize('expr', ["1 - 2", "1 + 12.5",
                                  "7 artichauts + 3 oranges",
                                  "-4 / 13", "4 % (7)"])
def test_eval_from_str_fails(expr):
    with pytest.raises(ValueError):
        eval_from_str(expr)


@pytest.mark.parametrize('expr', [None, ""])
def test_eval_from_str_empty(expr):
    with pytest.raises(AssertionError):
        eval_from_str(expr)