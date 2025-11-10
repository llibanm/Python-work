from dataclasses import dataclass
from tp3.linkedlist import (LinkedList,
                        ll_new,
                        ll_is_empty,
                        ll_len,
                        ll_str,
                        ll_head,
                        ll_tail,
                        ll_prepend,
                        ll_append,
                        ll_remove)


@dataclass
class Deque:
    ll: LinkedList


def d_new() -> Deque:
    return Deque(ll_new())


def d_is_empty(d: Deque) -> bool:
    return ll_is_empty(d.ll)


def d_len(d: Deque) -> int:
    return ll_len(d.ll)


def d_str(d: Deque) -> str:
    return ll_str(d.ll)


def d_front(d: Deque) -> int:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to get front of an empty deque')
    return ll_head(d.ll).item


def d_rear(d: Deque) -> int:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to get rear of an empty deque')
    return ll_tail(d.ll).item


def d_push_front(d: Deque, item: int) -> Deque:
    ll_prepend(d.ll, item)
    return d


def d_push_rear(d: Deque, item: int) -> Deque:
    ll_append(d.ll, item)
    return d


def d_pop_front(d: Deque) -> Deque:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to pop the front of an empty deque')
    # TODO: complete the missing part
    return d


def d_pop_rear(d: Deque) -> Deque:
    if ll_is_empty(d.ll):
        raise IndexError('Unable to pop the rear of an empty deque')
    # TODO: complete the missing part
    return d