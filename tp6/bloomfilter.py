from dataclasses import dataclass


@dataclass
class BloomFilter:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("BloomFilter class not implemented yet")


def bf_new() -> BloomFilter:
    raise NotImplementedError("bf_new function not implemented yet")


def bf_insert(bf: BloomFilter, word: str) -> BloomFilter:
    raise NotImplementedError("bf_insert function not implemented yet")


def bf_lookup(bf: BloomFilter, word: str) -> bool:
    raise NotImplementedError("bf_lookup function not implemented yet")
