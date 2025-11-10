from tp1.power import power , superpower
import pytest


POWER_CASES =               [(0, 0, 1),     # (a, n, expected power(a, n))
                             (1, 0, 1),
                             (2, 0, 1),
                             (42, 0, 1),
                             (0, 1, 0),
                             (1, 1, 1),
                             (2, 1, 2),
                             (42, 1, 42),
                             (0, 3, 0),
                             (1, 3, 1),
                             (2, 3, 8),
                             (42, 3, 74088),
                             (0, 4, 0),
                             (1, 4, 1),
                             (2, 4, 16),
                             (42, 4, 3111696),
                             (0, 5, 0),
                             (1, 5, 1),
                             (2, 5, 32),
                             (42, 5, 130691232),
                             (0, 10, 0),
                             (1, 10, 1),
                             (2, 10, 1024),
                             (42, 10, 17080198121677824),
                             (0, 42, 0),
                             (1, 42, 1),
                             (2, 42, 4398046511104),
                             (42, 42, 150130937545296572356771972164254457814047970568738777235893533016064)]


@pytest.mark.parametrize(('a', 'n', 'expected'), POWER_CASES)
def test_power(a, n, expected):
    assert power(a, n) == expected


@pytest.mark.parametrize(('a', 'n', 'expected'), POWER_CASES)
def test_superpower(a, n, expected):
    assert superpower(a, n) == expected
