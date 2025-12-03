from dataclasses import dataclass
from typing import Iterator


@dataclass
class HashSet:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("HashSet class not implemented yet")


def hs_new() -> HashSet:
    raise NotImplementedError("hs_new function not implemented yet")


def hs_size(hs: HashSet) -> int:
    raise NotImplementedError("hs_size function not implemented yet")


def hs_is_empty(hs: HashSet) -> bool:
    raise NotImplementedError("hs_is_empty function not implemented yet")


def hs_member(hs: HashSet, e: str) -> bool:
    raise NotImplementedError("hs_member function not implemented yet")


def hs_iterate(hs: HashSet) -> Iterator[str]:
    raise NotImplementedError("hs_iterate function not implemented yet")


def hs_insert(hs: HashSet, e: str) -> HashSet:
    raise NotImplementedError("hs_insert function not implemented yet")


def hs_delete(hs: HashSet, e: str) -> HashSet:
    raise NotImplementedError("hs_delete function not implemented yet")


def hs_union(first: HashSet, second: HashSet, in_place: bool = False) -> HashSet:
    raise NotImplementedError("hs_union function not implemented yet")


def hs_intersection(first: HashSet, second: HashSet) -> HashSet:
    raise NotImplementedError("hs_intersection function not implemented yet")


def hs_difference(first: HashSet, second: HashSet) -> HashSet:
    raise NotImplementedError("hs_difference function not implemented yet")
