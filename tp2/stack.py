from dataclasses import dataclass
from tp2.arraylist import (ArrayList,
                       al_new,
                       al_str,
                       al_len,
                       al_is_empty,
                       al_insert,
                       al_remove,
                       al_get)


@dataclass
class Stack:
    al: ArrayList


def s_new(n: int = 10) -> Stack:
    assert n >= 0
    return Stack(al_new(n))  # an empty stack is a stack with an empty array


def s_size(s: Stack) -> int:
    return al_len(s.al)


def s_is_empty(s: Stack) -> bool:
    return al_is_empty(s.al)


def s_str(s: Stack) -> str:
    return al_str(s.al)


def s_push(s: Stack, item: int) -> Stack:
    """Push item onto the stack. May raise an OverflowError."""
    al_insert(s.al, al_len(s.al), item)
    return s


def s_pop(s: Stack) -> Stack:
    """Pop the first element from the stack.

    Notes:
        Carefully define the behavior of "poping“ an empty stack
        Following the list.pop() behavior, it raises an IndexError
    """
    if s_is_empty(s):
        raise IndexError("Unable to pop an empty stack")
    else:
        al_remove(s.al, al_len(s.al) - 1)
    return s


def s_top(s: Stack) -> int:
    if s_is_empty(s):
        raise IndexError("Unable to get the top of an empty stack")
    else:
        return al_get(s.al, al_len(s.al) - 1)


if __name__ == '__main__':
    s: Stack = s_new()

    print('>>> push <<<')
    s_push(s, 0)
    s_push(s, 1)
    s_push(s, 2)
    s_push(s, 3)
    s_push(s, 4)
    print(s_str(s))

    print('>>> top <<<')
    print(s_top(s))

    print('>>> pop <<<')
    print(s_str(s_pop(s)), s_top(s))
    print(s_str(s_pop(s)), s_top(s))
    print(s_str(s_pop(s)), s_top(s))
    print(s_str(s_pop(s)), s_top(s))
    print(s_str(s_pop(s)))

    print('>>> pop/top empty list <<<')
    try:
        s_top(s)
    except IndexError:
        print("top une liste vide")
    try:
        s_pop(s)
    except IndexError:
        print("pop une liste vide")
