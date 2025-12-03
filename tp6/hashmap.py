from dataclasses import dataclass


@dataclass
class Item:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("Item class not implemented yet")


@dataclass
class HashMap:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("HashMap class not implemented yet")


def hm_size(aa: HashMap) -> int:
    raise NotImplementedError("hm_size function not implemented yet")


def hm_is_empty(aa: HashMap) -> bool:
    raise NotImplementedError("hm_is_empty function not implemented yet")


# TODO: complete hm_new parameters
def hm_new() -> HashMap:
    raise NotImplementedError("hm_new function not implemented yet")


def hm_get(aa: HashMap, k: str) -> int | None:
    raise NotImplementedError("hm_get function not implemented yet")


def hm_put(aa: HashMap, v: int, k: str) -> None:
    raise NotImplementedError("hm_put function not implemented yet")


def hm_delete(aa: HashMap, k: str) -> None:
    raise NotImplementedError("hm_delete function not implemented yet")


def hm_str(aa: HashMap) -> str:
    raise NotImplementedError("hm_str function not implemented yet")
