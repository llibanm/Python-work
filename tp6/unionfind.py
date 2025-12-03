from __future__ import annotations
from dataclasses import dataclass


@dataclass
class UnionFind:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("UnionFind class not implemented yet")


def uf_new(n: int = 10) -> UnionFind:
    raise NotImplementedError("uf_new function not implemented yet")


def uf_size(uf: UnionFind) -> int:
    raise NotImplementedError("uf_size function not implemented yet")


def uf_find(uf: UnionFind, x: int) -> int:
    raise NotImplementedError("hs_member function not implemented yet")


def uf_union(uf: UnionFind, x: int, y: int) -> UnionFind:
    raise NotImplementedError("uf_union function not implemented yet")
