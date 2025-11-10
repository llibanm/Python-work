__all__ = ['StaticArray', 'alloc', 'nops', 'reset_nops', 'list_to_array', 'array_to_list', 'random_array']

from ctypes import Array, c_int64, sizeof
import random
import sys


class StaticArray:
    """
    User-defined type of static arrays of integer.

    Attributes:
        _arr (c_int.Array): static array of fixed-size integers
        _get_count (int): number of read ops
        _set_count (int): number of write ops

    Properties:
        _count (dict of str: int): number of read and write operations

    Class Attributes:
        _signed_limit (int): max integer value to store in the array

    Methods:
        reset_count(str): reset counter of read and/or write operations
        to_list(): create a list of integers from a static array

    Operations (Dunder Methods):
        repr(`obj`): raw string representation of the static array `obj`
        str(`obj`): printable string representation of the static array `obj`
        len(`obj`): length of the static array `obj`
        `obj`[i]: access the ith element of the static array `obj`
        `obj`[i]=: write the ith element of the static array `obj`

    Notes:
        Equality is shallow equality (reference to the exact same array)
    """

    # Max integer value (int64) as a class attribute
    # Values must be in [-signed_limit, +signed_limit -1]
    signed_limit = 1 << (sizeof(c_int64) * 8 - 1)

    def __init__(self, m: int = 10):
        """`StaticArray` constructor

        Args:
            m (int, optional): size of the static array (default: 10)

        See:
            `alloc` function.
        """

        def _alloc(m: int) -> Array:
            """
            Helper function to allocate contiguous memory for static arrays.

            Uses C library
            Notes:
                Not intended to be visible outside/exported
            """
            assert 0 <= m <= sys.maxsize // 8
            # m <= (sys.maxsize // 8) is the usual limit for any python container (with 64bit values)
            # sys.maxsize := (1 << 63) - 1 = 9_223_372_036_854_775_807 on 64bit OS
            # warning: the memory limit, probably reached *far before* the limit on m value
            int_array = c_int64 * m
            return int_array()

        self._arr: Array = _alloc(m)
        self._get_count: int = 0
        self._set_count: int = 0

#    @staticmethod
#    def array(m: int):
#        return ArrayInt(m)

    def __repr__(self):
        return f"{self._arr!r}"

    def __str__(self):
        return f"[{', '.join(str(i) for i in self._arr)}]"

    def __setitem__(self, key: int, value: int):
        if not (-self.signed_limit <= value < self.signed_limit):
            raise OverflowError(f"Value {value!r} is out of integer range (64bits)")
        if not (0 <= key < len(self)):
            raise IndexError(f"Index {key!r} out of bounds")
        self._arr[key] = value
        self._set_count += 1

    def __getitem__(self, key: int):
        if not isinstance(key, int):     # prevent from a slice object (and any wrong key btw)
            raise ValueError(f"Index {key!r} must be an integer")
        if not (0 <= key < len(self)):
            raise IndexError(f"Index {key!r} out of bounds")
        self._get_count += 1
        return self._arr[key]

    def __len__(self):
        return len(self._arr)

    __iter__ = None     # prevent from iterating on array items
    # (def __iter__(self) raising an Error still considers type as Iterable!)

    @property
    def count(self):
        """See: `nops` function."""
        return {'nread': self._get_count, 'nwrite': self._set_count}

    def reset_count(self, mode: str = 'rw'):
        """See: `reset_nops` function."""
        if mode not in ('r', 'w', 'rw'):
            raise ValueError(f"mode {mode} not recognized. Valid modes are 'r', 'w' and 'rw'")
        if mode in ('w', 'rw'):
            self._set_count = 0
        if mode in ('r', 'rw'):
            self._get_count = 0

    def to_list(self) -> list[int]:
        return [self._arr[i] for i in range(len(self))]


    @staticmethod
    def from_list(l: list[int] | None) -> "StaticArray":
        """See: `list_to_array` function."""
        if l is None: l = []
        sarr = StaticArray(len(l))
        for i in range(len(sarr)):
            sarr[i] = l[i]
        sarr.reset_count()
        return sarr


    @classmethod
    def random_array(cls, m: int = 10, a: int = 0, b: int = 99, sorted: bool = False) -> 'StaticArray':
        """See: `random_array` function."""
        assert -cls.signed_limit <= a <= b < cls.signed_limit, f"Invalid range [{a}, {b}]"
        random.seed()
        t: list[int] = random.choices(range(a, b + 1), k=m)
        if sorted:
            t.sort()
        return cls.from_list(t)



def alloc(m: int) -> StaticArray:
    """
    StaticArray factory.

    Args:
        m (int): size of the array

    Returns:
        StaticArray: an array of size m filled with value 0

    Notes:
        To be used instead of the constructor StaticArray().
    """
    if m < 0:
        raise ValueError(f"Invalid size {m=}. It must be a natural number")
    return StaticArray(m)


def nops(sarr: StaticArray) -> dict[str, int]:
    """
    Number of read and write operations on a static array of integers.

    Args:
        sarr (StaticArray): static array of integers

    Returns:
        dict of (str: int): nread and nwrite numbers of operations.
                            The output format is like {'nread': 0, 'nwrite': 0}

    Notes:
        Return type should be a (named)tuple.
    """
    return sarr.count


def reset_nops(sarr: StaticArray, mode: str = 'rw') -> None:
    """
    Reset the number of read and write operations on a static array of integers.

    Args:
        sarr (StaticArray): static array of integers
        mode (str, optional): read 'r' or write 'w' counter, or both 'rw' (default: 'rw')
    """
    sarr.reset_count(mode)


def list_to_array(l: list[int] | None) -> StaticArray:
    """
    Create a new StaticArray from a list of integers.

    Raises:
        OverflowError: an integer value from the list is too large (restricted to int64)
    """
    return StaticArray.from_list(l)


def array_to_list(tab: StaticArray) -> list[int]:
    """Create a list of integers from a StaticArray."""
    return tab.to_list()


def random_array(m: int = 10, a: int = 0, b: int = 99, sorted: bool = False) -> StaticArray:
    """
    Generate a static array of random integers

    Args:
        m (int): size of the array (default: 10)
        a (int, optional): lower bound of the range of integer values (default: 0)
        b (int, optional): upper bound of the range of integer values (default: 99)
        sorted (bool, optional): sort the array (default: False)

    Returns:
        StaticArray: static array of m random integers in [a, b]

    Raises:
        ValueError: the range {a..b} is incorrect
        OverflowError: the integer values a and b are too large (restricted to int64)

    """
    if a < -StaticArray.signed_limit or b >= StaticArray.signed_limit:
        raise OverflowError(f"Invalid range [{a}, {b}]")
    if not a <= b:
        raise ValueError(f"Invalid range [{a}, {b}]")
    return StaticArray.random_array(m, a, b, sorted)


if __name__ == '__main__':
    # comprehensive example
    tab: StaticArray = alloc(5)               # allocate a new fresh array of 5 contiguous integers
    print(tab)                                # print [0, 0, 0, 0, 0] on stdout
    tab[2] = 2                                # write the third value => [0, 0, 2, 0, 0]
    for i in range(len(tab)):                 # loop over the indexes of the array, from 0 to the length - 1
        print(i, tab[i])                      # => 0 0\\ 1 0\\ 2 2\\ 3 0\\ 4 0
    print(nops(tab))                          # => {'nread': 5, 'nwrite': 1}
    reset_nops(tab)                           # reset read/write counts
    print(tab, nops(tab))                     # => [0, 0, 2, 0, 0] {'nread': 0, 'nwrite': 0}
    #for e in tab: print(e)                   # TypeError: 'StaticArray' object is not iterable
    #x = tab[1:3]                             # ValueError: Index slice(1, 3, None) must be an integer
    tab2 = random_array(10, 0, 2, True)   # create a sorted array of 10 random integers
    print(f"{tab2=!s}")                       # print on stdout (values between 0 and 2)
    print(f"{nops(tab2)=}")                   # => nops(tab2)={'nread': 0, 'nwrite': 0}