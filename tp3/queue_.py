# content of tp3/queue_.py
from dataclasses import dataclass


@dataclass
class Queue:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method below
    def __post_init__(self):
        raise NotImplementedError("Queue class not yet implemented")


def q_new(n: int = 10) -> Queue:
    raise NotImplementedError("Queue q_new function not yet implemented")


def q_size(q: Queue) -> int:
    raise NotImplementedError("Queue q_size function not yet implemented")


def q_is_empty(q: Queue) -> bool:
    raise NotImplementedError("Queue q_is_empty function not yet implemented")


def q_is_full(q: Queue) -> bool:
    raise NotImplementedError("Queue q_is_full function not yet implemented")


def q_str(q: Queue) -> str:
    raise NotImplementedError("Queue q_str function not yet implemented")


def q_enqueue(q: Queue, item: int) -> Queue:
    raise NotImplementedError("Queue q_enqueue function not yet implemented")


def q_dequeue(q: Queue) -> Queue:
    raise NotImplementedError("Queue q_dequeue function not yet implemented")


def q_rear(q: Queue) -> int:
    raise NotImplementedError("Queue q_rear function not yet implemented")


def q_front(q: Queue) -> int:
    raise NotImplementedError("Queue q_front function not yet implemented")