# content of tp3/stack.py
from dataclasses import dataclass
from tp3.deque import (Deque,d_new,d_is_empty,d_front,d_len,d_pop_front,d_pop_rear,d_push_front,d_push_rear
                       ,d_rear,d_str)

@dataclass
class Stack:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method below
   deque : Deque


def s_new(n: int = 10) -> Stack:
    raise NotImplementedError("Stack s_new function not yet implemented")
      

def s_size(s: Stack) -> int:
    raise NotImplementedError("Stack s_size function not yet implemented")


def s_is_empty(s: Stack) -> bool:
    raise NotImplementedError("Stack s_is_empty function not yet implemented")


def s_str(s: Stack) -> str:
    raise NotImplementedError("Stack s_str function not yet implemented")


def s_push(s: Stack, item: int) -> Stack:
    raise NotImplementedError("Stack s_push function not implemented yet")


def s_pop(s: Stack) -> Stack:
    raise NotImplementedError("Stack s_pop function not implemented yet")


def s_top(s: Stack) -> int:
    raise NotImplementedError("Stack s_top function not implemented yet")
