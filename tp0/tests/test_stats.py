from tp0.stats import update_stats_data, release_stats  # import the functions to test
import pytest
import math             # math.inf, -math.inf
import random           # generate random numbers
import statistics       # compute mean and standard deviation


def forge_acc(numbers: list[int]) -> list[int]:
    """
    Helper function to forge an accumulator from the stream.

    Args:
        numbers (list[int]): list -- stream -- of numbers.

    Returns:
        list[int]: accumulator [min, max, sum, sum of squares, count].
    """
    return [min(numbers) if numbers else math.inf,
            max(numbers) if numbers else -math.inf ,
            sum(numbers),
            sum(x ** 2 for x in numbers),
            len(numbers)]


def forge_stats(numbers: list[int]) -> dict[str, float]:
    """
    Helper function to forge stats from the stream.

    Args:
        numbers (list[int): list -- stream -- of numbers.

    Returns:
        dict[str, float]: statistics {'min': min, 'max': max, 'mean': mean, 'std-dev': standard deviation}.
    """
    return {'min': min(numbers),
            'max': max(numbers),
            'mean': statistics.fmean(numbers),
            'std-dev': statistics.pstdev(numbers)}


@pytest.fixture
def acc_zero():
    return [math.inf, -math.inf, 0, 0, 0] # min, max, sum, sum of squares, count


@pytest.fixture
def random_numbers():
    return random.choices([*range(101)], k=43)


############################
########## Tests ###########
############################


############# Function update_stats_data #############

@pytest.mark.parametrize(('value', 'expected'),[(0, [0, 0, 0, 0, 1]),
                                                (42, [42, 42, 42, 42 ** 2, 1]),
                                                (100, [100, 100, 100, 10_000, 1])])
def test_update_stats_data_single_number(acc_zero, value, expected):
    update_stats_data(acc_zero, value)
    assert acc_zero == expected


@pytest.mark.parametrize('size', [*range(42)])
def test_update_stats_data_full_stream(random_numbers, size):
    stream = random_numbers[:size]      # stream is a size-prefix of random_numbers
    val = random_numbers[size]          # next value in the stream
    # acc before
    acc = forge_acc(stream)
    update_stats_data(acc, val)
    # acc after
    expected_acc = forge_acc(stream + [val])
    # actual test
    assert acc == expected_acc


############# Function release_stats #############

@pytest.mark.parametrize(('acc', 'expected'),[([0, 0, 0, 0, 1], {'min': 0, 'max': 0, 'mean': 0, 'std-dev': 0}),
                                                ([42, 42, 42, 42 ** 2, 1], {'min': 42, 'max': 42, 'mean': 42, 'std-dev': 0}),
                                                ([100, 100, 100, 10_000, 1], {'min': 100, 'max': 100, 'mean': 100, 'std-dev': 0})])
def test_release_stats_single_number(acc, expected):
    assert release_stats(acc) == expected


@pytest.mark.parametrize('size', [*range(1, 42)])       # size > 0
def test_release_stats_full_stream(random_numbers, size):
    stream = random_numbers[:size]      # stream is a size-prefix of random_numbers
    acc = forge_acc(stream)
    expected = forge_stats(stream)
    assert release_stats(acc) == pytest.approx(expected, 0.001)     # floating point comparison


def test_release_stats_div_by_zero(acc_zero):
    with pytest.raises(AssertionError) as excinfo:  # check the exception (AssertionError)
        release_stats(acc_zero)                     # count is null => division by zero for mean and std-dev
    assert str(excinfo.value) == 'Empty stream'     # check the exception message